FROM python:3.8.1-alpine

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY app.py /app

ENTRYPOINT ["python", "-u", "app.py" ]