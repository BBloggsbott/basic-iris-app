FROM python:3.10-buster

COPY model.joblib iris_app/model.joblib
COPY requirements.txt iris_app/requirements.txt
COPY app.py iris_app/app.py

WORKDIR iris_app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD uvicorn --port 8080 app:app