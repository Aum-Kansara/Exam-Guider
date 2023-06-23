from flask import Flask,render_template,request,send_from_directory,current_app
from pdfBuilder import generatePDF
import os
from pickle import load

app=Flask(__name__)
app.config["UPLOAD_FOLDER"]='static/pdfs'
filename='Question_Bank.pdf'
years=['2018', '2019', '2020', '2021', '2022']
chapters_list=["Introduction To Data Structure","Linear Data Struture","NonLinear Data Structure","Hashing And File Structure","Sorting & Searching"]

def loadQuestionsDF():
    questions_df=load(open("dsa_questions_df.pkl",'rb'))
    return questions_df

questions_df=loadQuestionsDF()

def getQuestionFromChapters(chapters,no_of_questions,selected_year):
    questions=[]
    questions_chapters=[]
    no_of_questions_per_chapter=no_of_questions//len(chapters)
    no_of_remaining_questions=no_of_questions-(no_of_questions_per_chapter*len(chapters))
    df=questions_df
    if selected_year:
        df=questions_df.loc[questions_df['Year']==selected_year]
        print(df)

    for chapter in chapters:
        selected_ques=df.loc[df['Chapter Titles']==chapters_list[int(chapter)-1]]['Question'].values.tolist()
        for i in selected_ques[:no_of_questions_per_chapter]:
            questions_chapters.append(chapters_list[int(chapter)-1])
            questions.append(i)

    if no_of_remaining_questions:   
        for qsn in df.loc[df['Chapter Titles']==chapters_list[int(chapters[0])-1]]['Question'].values.tolist()[(0-no_of_remaining_questions):]:
            questions.append(qsn)
    for i in range(no_of_remaining_questions):
        questions_chapters.append(chapters_list[int(chapters[0])-1])
    if no_of_questions>len(questions):
        no_of_questions=len(questions)
    return questions,questions_chapters

@app.route("/",methods=["GET","POST"])
def home_page():
    return render_template("index.html",years=years,chapters=chapters_list,chapters_len=len(chapters_list))

@app.route("/generate",methods=["GET","POST"])
def pdfGenerate():
    if request.method=="POST":
        selected_year=request.form.get('YearSelection')
        selected_chapters=request.form.get('chapters_txt').strip().split()
        no_of_chapters=len(selected_chapters)
        no_of_questions=request.form.get('no_of_que')
        questions,questions_chapters=getQuestionFromChapters(selected_chapters,int(no_of_questions),selected_year)
        generatePDF(filename,selected_year,selected_chapters,no_of_questions,questions,no_of_chapters,questions_chapters)
        uploads=os.path.join(current_app.root_path,app.config['UPLOAD_FOLDER'])
        return send_from_directory(directory=uploads,path=filename,as_attachment=True)
    return render_template("index.html",years=years,chapters=chapters_list)


if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True)
