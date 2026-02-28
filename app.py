from google import genai
from flask import Flask,render_template,request,jsonify
import joblib
import numpy as np
import os
Client=genai.Client(api_key="GEMINI_KEY")

model=joblib.load("employment_model.pkl")
scaler=joblib.load("scaler.pkl")
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():

    education = int(request.form.get("education"))
    internship = int(request.form.get("internship"))
    region = int(request.form.get("region"))
    age = float(request.form.get("age"))
    gpa = float(request.form.get("gpa"))
    ranking = int(request.form.get("ranking"))

    input_data = np.array([[education,
                            internship,
                            region,
                            age,
                            gpa,
                            ranking]])

    input_scaled = scaler.transform(input_data)

    probability = model.predict_proba(input_scaled)[0][1]
    prediction = "Employed" if probability > 0.5 else "Unemployed"

    return jsonify({
        "prediction": prediction,
        "probability": round(probability*100, 2)
    })
if __name__ == "__main__":
    app.run()