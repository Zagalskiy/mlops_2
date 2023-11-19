from flask import Flask, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello from Flask!")

@app.route("/predict/<int:age>/<int:education_num>/<int:sex>/<int:capital_gain>")
def predict(age, education_num, sex, capital_gain):
    with open("./models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
