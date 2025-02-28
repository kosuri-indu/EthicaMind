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
            {"role": "system", "content": "You are an ethical AI assistant."},
            {"role": "user", "content": question}
        ],
        "max_tokens": 200
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response generated.")
    
    return f"Error: {response.status_code} - {response.text}"

def generate_scenario_and_insights(prompt):
    scenario_prompt = f"🔍 Scenario Generation and ethical insights: AI crafts real-world ethical dilemmas with key actors, risks, and benefits. Prompt: {prompt}"
    return generate_response(scenario_prompt)