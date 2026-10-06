from flask import Flask, request, render_template, jsonify
from chatbot import get_qa_bot
import os

app = Flask(__name__)
qa_bot = get_qa_bot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question")
    if not user_input:
        return jsonify({"answer": "Please ask a question."})
    answer = qa_bot.run(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)