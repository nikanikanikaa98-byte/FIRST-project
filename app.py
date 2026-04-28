from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OK from CD"

@app.route("/health")
def health():
    return jsonify(status="ok")
