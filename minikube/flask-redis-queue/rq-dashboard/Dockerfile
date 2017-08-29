FROM python:3.6.2

COPY . /opt/www
WORKDIR /opt/www

RUN pip install -r /opt/www/requirements.txt

EXPOSE 9181
CMD ["rq-dashboard", "--port", "9181", \
                     "--redis-host", "redis-master", \
                     "--redis-port", "6379"]