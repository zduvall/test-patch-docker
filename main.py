from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get():
    return {"message": "get"}


@app.post("/")
async def post():
    return {"message": "post"}


@app.put("/")
async def put():
    return {"message": "put"}


@app.patch("/")
async def patch():
    return {"message": "patch"}


@app.delete("/")
async def delete():
    return {"message": "delete"}


@app.head("/")
async def head():
    return  # body ignored


@app.options("/")
async def options():
    return {"message": "options"}
