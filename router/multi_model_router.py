from flask import Flask, request, jsonify
from ollama import Client

client = Client(host="http://localhost:11434")

app = Flask(__name__)

def choose_model(prompt):

    p = prompt.lower()

    if "code" in p or "python" in p or "javascript" in p:
        return "codellama"

    if len(prompt) < 100:
        return "phi3"

    return "mistral"


@app.route("/api/query", methods=["POST"])
def query():

    prompt = request.json["prompt"]

    model = choose_model(prompt)

    response = client.generate(
        model=model,
        prompt=prompt
    )

    return jsonify({
        "model": model,
        "response": response["response"]
    })


app.run(host="0.0.0.0", port=5000)
