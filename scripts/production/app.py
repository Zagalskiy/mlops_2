from flask import Flask, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello from Flask!")
