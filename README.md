# Problem with `PATCH` + docker

Steps to reproduce:

- In this directory, run:

  - `$ docker compose build`
  - `$ docker compose up`

- Test requests sent to `http://0.0.0.0:8000/` for all methods in `main.py`
- All requests will show 200 resopnse in terminal...

```
test-patch-docker ... "GET / HTTP/1.1" 200 OK
test-patch-docker ... "POST / HTTP/1.1" 200 OK
test-patch-docker ... "PUT / HTTP/1.1" 200 OK
test-patch-docker ... "PUT / HTTP/1.1" 200 OK
test-patch-docker ... "PATCH / HTTP/1.1" 200 OK
test-patch-docker ... "DELETE / HTTP/1.1" 200 OK
test-patch-docker ... "HEAD / HTTP/1.1" 200 OK
test-patch-docker ... "OPTIONS / HTTP/1.1" 200 OK
```

- ...however the patch response never makes it to the client

Tested this in multiple browsers and with Postman
