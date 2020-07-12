# Flask+uWSGI+Nginx+Docker Demo


- [Flask+uWSGI+Nginx+Docker Demo](#flaskuwsginginxdocker-demo)
  - [目的&需求](#目的需求)
  - [資料夾結構](#資料夾結構)
  - [測試用 API](#測試用-api)


目的&需求
---
- 把一個Flask專案打包成docker
- 需加上```uWSGI``` & ```Nginx```
- 有時需要看nginx log 或是 uWSGI log , 因此需獨立出來(暫時的做法)



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

