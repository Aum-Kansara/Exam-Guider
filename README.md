# Exam Guider
## Question Bank Generator (For Data Structures And Algorithms)

## Live on URL : [https://exam-guider-aum-kansara.koyeb.app/](https://exam-guider-aum-kansara.koyeb.app/)

### Classified Questions which are Extracted from exam paper's pdf (programmatically)
### Video Demo : 

https://github.com/Aum-Kansara/Exam-Guider/assets/117375317/759feffe-70b2-4509-8a4e-2d09e2824c35


### Generated PDF :
![Output](https://github.com/Aum-Kansara/Exam-Guider/assets/117375317/27fa205f-4fb4-419e-90ce-b8ac03c20e4a)

## Run Locally
### 1. Docker 
- Run following commands

      docker pull aumkansara/question_bank_generator:latest

      docker run -p 8000:8000 aumkansara/question_bank_generator:latest

- App running on [localhost:8000](http://127.0.0.1:8000)

### 2. Clone Git Repository
- Run
    
      git clone https://github.com/Aum-Kansara/Exam-Guider.git

      cd Exam-Guider/

    -   Using Virtual Environment

            pip3 install virtualenv

            virtualenv venv
        
    1. Linux

            source venv/bin/activate
    
    2. Windows

            source venv/scripts/activate

- Next steps
      
      pip3 install -r requirements.txt

      gunicorn app:app

    - Use host=0.0.0.0 to publicly access service
        
          gunicorn app:app --host=0.0.0.0

- App running on [localhost:8000](http://127.0.0.1:8000)


## Thank You






