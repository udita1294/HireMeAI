import json
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel
from pypdf import PdfReader

load_dotenv()


app = FastAPI()

# pdf extraction
def read_pdf(file_path: Path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


@app.get("/")
def home():
    resume_text = read_pdf(Path("my_resume.pdf"))
    print(resume_text)
    return {
        "message" : "Resume parsed successfully!"
    }


