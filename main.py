from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def getting_started():
    return {"data": "Introduction to CI/CD"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
