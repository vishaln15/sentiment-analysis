from flask import Flask, jsonify, request, render_template
from utils import predict_pipeline
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    data = request.form["text"]
    try:
        sample = data
    except KeyError:
        return jsonify({"error": "No text was passed!"})

    sample = [sample]
    preds = predict_pipeline(sample)
    output = preds[0]["label"]
    return render_template("index.html", prediction_text=f"The type of text is predicted as {output}")

app.run(port=int(os.environ.get("PORT", 5000)), host="0.0.0.0")
