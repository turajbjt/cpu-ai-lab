#!/usr/bin/python

from flask import Flask, request, jsonify
from agents.coordinator import run_goal

app = Flask(__name__)

@app.route("/api/goal", methods=["POST"])
def handle_goal():
    data = request.json
    goal = data.get("goal")
    if not goal:
        return jsonify({"error": "No goal provided"}), 400

    try:
        result = run_goal(goal)
        return jsonify({"goal": goal, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
