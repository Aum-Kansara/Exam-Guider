FROM python:3.8-slim-buster

RUN apt-get update && apt-get install

RUN apt install fontconfig libfreetype6 libjpeg62-turbo libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base wget -y 

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb

RUN dpkg -i wkhtmltox_0.12.6-1.buster_amd64.deb

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .

CMD [ "gunicorn", "app:app","--bind","0.0.0.0:8000"]