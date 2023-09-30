from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get():
    return {"method": "get"}


@app.post("/")
async def post():
    return {"method": "post"}


@app.put("/")
async def put():
    return {"method": "put"}


@app.patch("/")
async def patch():
    return {"method": "patch"}


@app.delete("/")
async def delete():
    return {"method": "delete"}


@app.head("/")
async def head():
    return  # body ignored


@app.options("/")
async def options():
    return {"method": "options"}
