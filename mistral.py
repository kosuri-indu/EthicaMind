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
        "max_tokens": 100000
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

    5. Justification & Counterarguments:
       - Provide a core ethical justification supporting the issue.
       - Present at least three strong counterarguments against the issue.
       - Use real-world examples, logical reasoning, and ethical principles.

    6. **Generate a Detailed Summary**:
       - Provide a longer, more in-depth summary (4-6 sentences).
       - Clearly explain the dilemma, its significance, and key ethical takeaways.

    7. Balanced Conclusion:
       - Weigh both sides and provide a fair, reasoned conclusion.

    Example Prompt:  
    Should AI be used for grading exams?

    Example Response (JSON format):  
    {{
        "summary": "AI-driven grading offers efficiency and consistency, but fairness concerns remain. While automation reduces human bias and speeds up the process, it may not account for subjectivity in assessments. Some argue that AI ensures standardized grading, but others worry about over-reliance on algorithms. Ethical considerations include fairness, accountability, and the need for human oversight. Schools implementing AI grading should establish clear guidelines and regularly audit results. A balanced approach integrating AI with human review may be the best path forward.",
        "scenario": "AI-driven exam grading.",
        "key_actors": ["Students", "Teachers", "Administrators"],
        "risks": ["Bias", "Lack of human judgment", "Privacy concerns"],
        "benefits": ["Faster grading", "Reduced workload", "Standardized scoring"],
        "ethical_perspectives": {{
            "utilitarianism": {{"analysis": "Maximizes efficiency, potential bias.", "score": 7}},
            "deontology": {{"analysis": "Fairness, transparency.", "score": 6}},
            "virtue_ethics": {{"analysis": "Fairness, empathy.", "score": 8}}
        }},
        "justification": "AI in grading ensures faster and fairer assessments but may lack human oversight.",
        "pros": ["Efficiency", "Standardization", "Scalability"],
        "cons": ["Bias in training data", "Lack of subjective assessment"],
        "counterarguments": [
            "AI may reinforce biases in historical data.",
            "It lacks human intuition for subjective answers.",
            "Over-reliance may devalue teachers' roles."
        ],
        "conclusion": "AI can assist grading, but human oversight is necessary to ensure fairness."
    }}

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)

def generate_scenario_comparisons(prompt):
    structured_prompt = f"""
    Scenario Comparison Mode - Compare multiple ethical choices side-by-side to see the best approach.

    AI must construct multiple structured ethical dilemmas and analyze them based on the given prompt.

    ### Instructions:
    Generate 6 different scenarios based on the prompt. For each scenario, provide the following details in JSON format:
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
    [
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
        }},
        ...
    ]

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)

def generate_debate(prompt):
    structured_prompt = f"""
    Ethical Debate Generation

    AI must construct a structured ethical debate based on the given prompt.

    ### Instructions:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders.

    3. Present Arguments For and Against:
       - Provide detailed arguments for both sides.

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
        "arguments_for": ["Faster grading", "Reduced workload", "Standardized scoring"],
        "arguments_against": ["Bias", "Lack of human judgment", "Privacy concerns"],
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

def generate_justification(prompt):
    structured_prompt = f"""
    Ethical Justification Generation

    AI must construct a structured ethical justification based on the given prompt.

    ### Instructions:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders.

    3. Provide a Justification for the Decision:
       - Provide a detailed justification for the decision.

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
        "justification": "AI-driven grading maximizes efficiency and reduces teacher workload, but potential bias must be addressed.",
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

def generate_scenario_comparisons(prompt):
    structured_prompt = f"""
    Scenario Comparison Mode - Compare multiple ethical choices side-by-side to see the best approach.

    AI must construct multiple structured ethical dilemmas and analyze them based on the given prompt.

    ### Instructions:
    Generate 6 different scenarios based on the prompt. For each scenario, provide the following details in JSON format:
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
    [
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
        }},
        ...
    ]

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)

def generate_debate(prompt):
    structured_prompt = f"""
    Ethical Debate Generation

    AI must construct a structured ethical debate based on the given prompt.

    ### Instructions:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders.

    3. Present Arguments For and Against:
       - Provide detailed arguments for both sides.

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
        "arguments_for": ["Faster grading", "Reduced workload", "Standardized scoring"],
        "arguments_against": ["Bias", "Lack of human judgment", "Privacy concerns"],
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

def generate_justification(prompt):
    structured_prompt = f"""
    Ethical Justification Generation

    AI must construct a structured ethical justification based on the given prompt.

    ### Instructions:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders.

    3. Provide a Justification for the Decision:
       - Provide a detailed justification for the decision.

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
        "justification": "AI-driven grading maximizes efficiency and reduces teacher workload, but potential bias must be addressed.",
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
