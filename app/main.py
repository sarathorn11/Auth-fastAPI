from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return "hello world"
    
    
