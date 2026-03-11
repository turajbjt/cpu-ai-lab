from flask import Flask, request, jsonify
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

app = Flask(__name__)


@app.route("/agent", methods=["POST"])
def agent():

    prompt = request.json["prompt"]

    response = llm.invoke(prompt)

    return jsonify({
        "response": response
    })


app.run(host="0.0.0.0", port=7000)
