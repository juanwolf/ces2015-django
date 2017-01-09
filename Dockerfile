FROM ubuntu:xenial

MAINTAINER Jean-Loup Adde "jean-loup.adde@juanwolf.fr"

# Change bash to dash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN apt-get update
RUN apt-get install -y python3-dev python3-setuptools python3-pip libtiff-dev \
libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl-dev tk-dev python3-tk \
libpq-dev uwsgi-plugin-python3 libpcre3 libpcre3-dev gettext nodejs npm git sass
RUN npm install -g bower
RUN pip3 install virtualenv
RUN pip3 install uwsgi

RUN virtualenv /opt/virtualenvs/ces2015
RUN source /opt/virtualenvs/ces2015/bin/activate

ADD . /opt/ces2015

WORKDIR /opt/ces2015
RUN bower --allow-root install
RUN npm install -g grunt-cli
RUN npm install
RUN grunt

WORKDIR /opt/ces2015/ces2015
RUN /opt/virtualenvs/ces2015/bin/pip install -r /opt/ces2015/requirements.txt
RUN /opt/virtualenvs/ces2015/bin/python manage.py compilemessages
RUN /opt/virtualenvs/ces2015/bin/python manage.py collectstatic --no-input

EXPOSE 8000
CMD uwsgi --ini=/opt/ces2015/ces2015.ini --pidfile=/opt/ces2015/site.pid

