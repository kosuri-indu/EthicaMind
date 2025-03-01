from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from flask_session import Session
from dotenv import load_dotenv
import os
from mistral import generate_scenario_and_insights, generate_scenario_comparisons, generate_debate, generate_justification, generate_chat_response
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
    try:
        prompt = session.get('prompt', '')
        insights = generate_scenario_and_insights(prompt)
        insights_json = json.loads(insights)
    except Exception as e:
        return redirect(url_for('error', error_message=str(e)))
    return render_template("insights.html", insights=insights_json)

@app.route("/scenarios")
def scenarios():
    try:
        prompt = session.get('prompt', '')
        scenarios = generate_scenario_comparisons(prompt)
        print(scenarios)
        scenarios_json = json.loads(scenarios)
    except Exception as e:
        return redirect(url_for('error', error_message=str(e)))
    return render_template("scenarios.html", scenarios=scenarios_json)

@app.route("/debate")
def debate():
    try:
        prompt = session.get('prompt', '')
        debate = generate_debate(prompt)
        debate_json = json.loads(debate)
        session['chat_history'] = [{"role": "system", "content": f"This was your scenario: {debate_json['scenario']}. What do you think?"}]
    except Exception as e:
        return redirect(url_for('error', error_message=str(e)))
    return render_template("debate.html", debate=debate_json)

@app.route("/debate_message", methods=["POST"])
def debate_message():
    data = request.get_json()
    message = data.get("message", "")
    chat_history = session.get('chat_history', [])
    chat_history.append({"role": "user", "content": message})
    response = generate_chat_response(message, chat_history)
    chat_history.append({"role": "assistant", "content": response})
    session['chat_history'] = chat_history
    return jsonify({"response": response})

@app.route("/justification")
def justification():
    try:
        prompt = session.get('prompt', '')
        justification = generate_justification(prompt)
        justification_json = json.loads(justification)
    except Exception as e:
        return redirect(url_for('error', error_message=str(e)))
    return render_template("justification.html", justification=justification_json)

@app.route("/error")
def error():
    error_message = request.args.get('error_message', 'An unknown error occurred.')
    return render_template("error.html", error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)