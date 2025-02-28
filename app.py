from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    question = data.get("question", "")

    # Static Response for Now
    response = {
        "scenario": f"Sample scenario for: {question}",
        "analysis": {
            "Utilitarianism": "This is the utilitarian perspective.",
            "Deontology": "This is the deontological perspective.",
            "Virtue Ethics": "This is the virtue ethics perspective."
        }
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
