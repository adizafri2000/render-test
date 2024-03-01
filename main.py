from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    #print(f"Request at '/' received at {datetime.now()}")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    #print(f"Request at '/hello/name' received at {datetime.now()}, name: {name}")
    return {"message": f"Hello {name}"}
