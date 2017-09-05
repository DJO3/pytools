FROM python:3.6.2
RUN apt-get update -y
RUN apt-get install -y vim
COPY ./ /opt/www/web
WORKDIR /opt/www/web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
