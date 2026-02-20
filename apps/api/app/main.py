from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project 2 API running"}
