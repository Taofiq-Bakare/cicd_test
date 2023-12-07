from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def getting_started():
    return {"data": "Introduction to CI/CD"}
