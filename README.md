# Problem with `PATCH` + docker

Steps to reproduce:

- In this directory, run:

  - `$ docker compose build`
  - `$ docker compose up`

- Send requests to `http://0.0.0.0:8000/` for all methods in `main.py`
- All will show 200 resopnse in terminal...

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

- ...however the response from the `patch` request alone never makes it to the client

Reproduced in multiple browsers and Postman

I have a 2020 MacBook Pro and noticed this problem before and after upgrading MacOS (timing by chance). Also in an effort to address it, I upgraded Docker, Uvicorn and FastApi. I don't remember the specific versions I had of Docker Engine and Compose previously, but here's the software I've reproduced this on otherwise:

| Software       | Versions                              |
| -------------- | ------------------------------------- |
| MacOS          | Ventura 13.0 & OS Sonoma 14.0         |
| Docker Desktop | 3.26.0 & 4.24.0                       |
| Docker Engine  | (earlier-version) & 24.0.6            |
| Docker Compose | (earlier-version) & v2.22.0-desktop.2 |
| Uvicorn        | 0.17.6 & 0.23.2                       |
| FastApi        | 0.82.0 & 0.103.2                      |
