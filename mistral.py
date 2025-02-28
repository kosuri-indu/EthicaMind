import os
import requests

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def generate_response(question):
    if not MISTRAL_API_KEY:
        return "Error: API key not found."

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "You are an AI assistant specializing in ethical decision making. Your responses should be in concise JSON format."},
            {"role": "user", "content": question}
        ],
        "max_tokens": 1000
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        try:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response generated.")
        except ValueError:
            return "Error: Invalid JSON response"
    
    return f"Error: {response.status_code} - {response.text}"

def generate_scenario_and_insights(prompt):
    structured_prompt = f"""
    Ethical Scenario & Insights Generation

    AI must construct a structured ethical dilemma and analyze it based on the given prompt.

    ### Instructions:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders.

    3. Analyze the Potential Risks and Benefits:
       - Clearly differentiate risks from benefits.

    4. Evaluate Using Ethical Theories:
       - Utilitarianism: Does this decision maximize overall happiness? Provide a score (0-10).
       - Deontology: Does it adhere to moral duties and rules? Provide a score (0-10).
       - Virtue Ethics: Does it promote good character and ethical behavior? Provide a score (0-10).

    Example Prompt:  
    Should AI be used for grading exams?

    Example Response (JSON format):  
    {{
        "scenario": "AI-driven exam grading.",
        "key_actors": ["Students", "Teachers", "Administrators"],
        "risks": ["Bias", "Lack of human judgment", "Privacy concerns"],
        "benefits": ["Faster grading", "Reduced workload", "Standardized scoring"],
        "ethical_perspectives": {{
            "utilitarianism": {{"analysis": "Maximizes efficiency, potential bias.", "score": 7}},
            "deontology": {{"analysis": "Fairness, transparency.", "score": 6}},
            "virtue_ethics": {{"analysis": "Fairness, empathy.", "score": 8}}
        }}
    }}

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)