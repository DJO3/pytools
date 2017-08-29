FROM python:3.6.2

COPY . /opt/www
WORKDIR /opt/www

RUN pip install -r /opt/www/requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]
