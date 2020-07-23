# Flask+uWSGI+Nginx+Docker Demo


- [Flask+uWSGI+Nginx+Docker Demo](#flaskuwsginginxdocker-demo)
  - [目的&需求](#目的需求)
  - [使用方法](#使用方法)
  - [測試用 API](#測試用-api)
  - [資料夾結構](#資料夾結構)
  - [參考資料](#參考資料)


目的&需求
---
- 把一個Flask專案打包成docker
- 需加上```uWSGI``` & ```Nginx```
- 有時需要看nginx log 或是 uWSGI log , 因此需獨立出來(暫時的做法)

使用方法
---

1. clone this repo

```bash
$git clone https://github.com/a607ernie/Flask-uWSGI-Nginx-Docker
```

2. run container

```bash
docker-compose up -d
```

3. then call [api](#測試用-api)


4. close docker-compose
```bash
docker-compose down -v
```

測試用 API
---

http://localhost/
```html
Python Flask in Docker!
A sample web-app for running Flask inside Docker.

API list :

[GET] /hi
[POST] /post_name
```

http://localhost/hi
```html
hi
```

http://localhost/post_name

body
```json
{
    "name":"json"
}
```

response

```
{
    "comment": "Hello json",
    "status": 200
}
```

資料夾結構
---
```
│  .dockerignore
│  app.ini
│  Dockerfile
│  requirements.txt
│  run.py
│  wsgi.py
│
├─app
│  │  __init__.py
│  │
│  ├─api
│  │  │  api_test.py
│  │  │
├─nginx
│  │  Dockerfile
│  │  flask_app.conf
│  │  nginx.conf
│  │
├─nginx_log
│  │  access.log
│  │  error.log
│  │
├─uwsgi_log
│  │  app.log
│  │
```

參考資料
---

- [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)
- [uwsgi-nginx-docker](https://github.com/tiangolo/uwsgi-nginx-docker)
