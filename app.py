from fastapi import FastAPI
from collector import get_ai_news

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/collect")
def collect():
    return get_ai_news()
