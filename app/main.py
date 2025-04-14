from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "✅ FastAPI is working on Render!"}

@app.get("/hello")
def hello():
    return {"hello": "world"}
