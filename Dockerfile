FROM python:3.10-buster

COPY build_model.py iris_app/build_model.py
COPY requirements.txt iris_app/requirements.txt
COPY app.py iris_app/app.py

WORKDIR iris_app/

RUN pip install -r requirements.txt
RUN python build_model.py


CMD uvicorn --host 0.0.0.0 --port 8080 app:app