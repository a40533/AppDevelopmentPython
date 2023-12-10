from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse


app = FastAPI()


@app.get("/test", response_class=JSONResponse)
def home():
    return {"test key": "test value",
            "test key2": "test value2",
            "test key3": "test value3"}


@app.get("/", response_class=PlainTextResponse)
def test_home():
    return "Hello World"
