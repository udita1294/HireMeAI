from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "HireMe API is running successfully!"
    }