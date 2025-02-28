from flask import Flask, request, render_template, jsonify, session
from flask_session import Session
from dotenv import load_dotenv
import os
from mistral import generate_scenario_and_insights
import json

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

app.config["SESSION_TYPE"] = os.getenv("SESSION_TYPE")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Session(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    question = data.get("question", "")

    session['prompt'] = question

    response = {
        "scenario": f"Sample scenario for: {question}",
        "analysis": {
            "Utilitarianism": "This is the utilitarian perspective.",
            "Deontology": "This is the deontological perspective.",
            "Virtue Ethics": "This is the virtue ethics perspective."
        }
    }
    
    return jsonify(response)

@app.route("/get_prompt")
def get_prompt():
    prompt = session.get('prompt', '')
    return jsonify({"prompt": prompt})

@app.route("/insights")
def insights():
    prompt = session.get('prompt', '')
    insights = generate_scenario_and_insights(prompt[5:])
    try:
        print(insights)
        insights_json = json.loads(insights)
        print(insights_json)
    except json.JSONDecodeError:
        insights_json = {"error": "Invalid JSON response from AI"}
    return render_template("insights.html", insights=insights_json)

@app.route("/scenarios")
def scenarios():
    return render_template("scenarios.html")

@app.route("/debate")
def debate():
    return render_template("debate.html")

@app.route("/justification")
def justification():
    return render_template("justification.html")

if __name__ == "__main__":
    app.run(debug=True)