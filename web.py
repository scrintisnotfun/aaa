
from flask import Flask, jsonify
from app.bot import get_recent_pets

app = Flask(__name__)

@app.route("/")
def home():
    return "Pet tracker is running!"

@app.route("/recent-pets")
def recent():
    return jsonify(get_recent_pets())

@app.route("/ping")
def ping():
    return "pong"
