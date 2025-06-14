from fastapi import FastAPI
from pydantic import BaseModel
import json
import openai

import os

openai.api_key = os.getenv("")

app = FastAPI()

# Load pre-scraped data
with open("tds_data.json") as f:
    db = json.load(f)


class QuestionRequest(BaseModel):
    question: str
    image: str = None


@app.post("/api/")
def answer(request: QuestionRequest):
    question = request.question

    # Combine TDS course + Discourse content
    content = db['tds_course'][:3000] + str(db['discourse'])[:3000]

    prompt = f"""You are a TDS Teaching Assistant. Use the following course and Discourse content to answer:

    {content}

    Q: {question}
    """

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role": "user",
                                                "content": prompt
                                            }])

    return {
        "answer":
        response['choices'][0]['message']['content'],
        "links": [{
            "url":
            "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34",
            "text": "More on TDS Discourse"
        }]
    }
