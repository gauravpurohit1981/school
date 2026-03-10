from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI

app = Flask(__name__)

endpoint = "https://nhsg-botproject.openai.azure.com/"
deployment = "gpt-4.1-mini"
api_key = "8SmkE0397OotLklprZcB1ktha3fesuM6c5I1Z9QVdR9IhKonQH8FJQQJ99CCACYeBjFXJ3w3AAABACOGNC9H"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for Newcastle High School for Girls."},
            {"role": "user", "content": user_message}
        ],
        max_completion_tokens=500
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
