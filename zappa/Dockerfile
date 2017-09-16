FROM python:3.6.2

RUN apt-get update -y && \
apt-get install -y vim && \
apt-get clean && \
useradd -ms /bin/bash py && \
pip install virtualenv virtualenvwrapper

COPY ./ /opt/www/web
USER py
WORKDIR /opt/www/web

ENV WORKON_HOME=~/.virtualenvs
ENV PROJECT_HOME=~/Devel

RUN echo "source /usr/local/bin/virtualenvwrapper.sh\nworkon main" >> ~/.bashrc
RUN bash -c "source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv main && pip install -r requirements.txt"

