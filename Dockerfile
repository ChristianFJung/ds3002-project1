FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install PyInquirer
RUN pip install prompt_toolkit==1.0.14

COPY . .



#ENTRYPOINT "python3 main.py" && /bin/bash