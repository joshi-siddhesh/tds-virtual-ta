from flask import Flask, request, jsonify
import openai
import base64
import os

app = Flask(__name__)
openai.api_key = os.getenv("")

@app.route("/api/", methods=["POST"])
def answer_question():
    data = request.get_json()
    question = data.get("question", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful TA for the TDS course."},
            {"role": "user", "content": question}
        ],
        temperature=0.2
    )

    answer_text = response['choices'][0]['message']['content']

    response = {
        "answer": answer_text,
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            }
        ]
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
