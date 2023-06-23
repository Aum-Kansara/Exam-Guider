import jinja2
import pdfkit
from os import remove



template_loader = jinja2.FileSystemLoader('./static')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template('question_bank_template.html')


def generatePDF(pdf_name,selected_year,selected_chapters,no_of_questions,questions,no_of_chapters,questions_chapters):
    context = {'selected_year':selected_year,"selected_chapters":selected_chapters,"no_of_questions":no_of_questions,"questions":questions,"no_of_chapters":no_of_chapters,"questions_chapters":questions_chapters}
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, pdf_name, configuration=config, css='basic_style.css',options={"enable-local-file-access": None})
    with open(pdf_name,'rb') as f:
        with open(f'static/pdfs/{pdf_name}','wb') as f1:
            for i in f:
                f1.write(i)
    remove(pdf_name)

if __name__=="__main__":
    selected_year='2022'
    selected_chapters=[1,2,3,4,5]
    no_of_questions=15
    questions=['Define following Terms: Derived data, Abstract Class, Generalization, Multiplicity,  Constrains.','Describe guidelines for use case Models.','Describe in detail the stages of Object-Oriented methodology.','What is software development process? Enlist steps of software development process?']
    generatePDF('new.pdf',selected_year,selected_chapters,no_of_questions,questions)