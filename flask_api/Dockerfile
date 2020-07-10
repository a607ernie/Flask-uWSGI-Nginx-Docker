FROM python:3.7
#FROM python:3.7-alpine

RUN mkdir /docker_api\
&&  mkdir /uwsgi_log

WORKDIR /docker_api

COPY . /docker_api

#RUN apk add --no-cache uwsgi-python3
#RUN pip install uwsgi
RUN pip install -r requirements.txt


#CMD [ "uwsgi","--http",":8000","--wsgi-file","wsgi.py" ]



#CMD ["uwsgi", "--ini", "app.ini"]