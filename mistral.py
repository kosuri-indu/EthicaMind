import json
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
            response_json = response.json()
            if "choices" in response_json and len(response_json["choices"]) > 0:
                return response_json["choices"][0]["message"]["content"]
            else:
                return "No response generated."
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
        "summary": "AI-driven grading offers efficiency and consistency, but fairness concerns remain. While automation reduces human bias and speeds up the process, it may not account for subjectivity in assessments. Some argue that AI ensures standardized grading, but others worry about over-reliance on algorithms. Ethical considerations include fairness, accountability, and the need for human oversight. Schools implementing AI grading should establish clear guidelines and regularly audit results. A balanced approach integrating AI with human review may be the best path forward.",
        "scenario": "AI for employee productivity monitoring is the scenario where artificial intelligence is used to track and evaluate employee performance. This approach aims to enhance productivity and resource allocation by providing data-driven insights. However, it raises concerns about privacy, employee stress, and the potential misuse of data. The debate centers around whether the benefits of AI monitoring outweigh the potential drawbacks and ethical implications.",
        "key_actors": [
                {{"name": "Employees", "role": "Monitored for productivity"}},
                {{"name": "Management", "role": "Oversee productivity"}},
                {{"name": "AI Developers", "role": "Develop monitoring tools"}}
            ],
            "risks": ["Privacy invasion", "Employee stress", "Potential misuse of data"],
            "benefits": ["Increased productivity", "Better resource allocation", "Data-driven decision making"],
            "ethical_perspectives": {{
                "utilitarianism": {{"analysis": "Focuses on productivity, potential stress.", "score": 6}},
                "deontology": {{"analysis": "Privacy concerns, duty to respect rights.", "score": 5}},
                "virtue_ethics": {{"analysis": "Balance between productivity and well-being.", "score": 7}}
            }}
    }}

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)

def generate_scenario_comparisons(prompt):
    structured_prompt = f"""
    Scenario Comparison Mode - Compare multiple ethical choices side-by-side to see the best approach.

    AI must construct exactly 6 structured ethical dilemmas and analyze them based on the given prompt.

    ### Instructions:
    Generate exactly 6 different scenarios based on the prompt. For each scenario, provide the following details in JSON format:
    1. Describe the Ethical Dilemma:
       - Provide a detailed background.
       - Explain the conflicting viewpoints.

    2. Identify the Key Actors:
       - List all the major stakeholders and their roles.

    3. Analyze the Potential Risks and Benefits:
       - Clearly differentiate risks from benefits.

    4. Evaluate Using Ethical Theories:
       - Utilitarianism: Does this decision maximize overall happiness? Provide a score (0-10).
       - Deontology: Does it adhere to moral duties and rules? Provide a score (0-10).
       - Virtue Ethics: Does it promote good character and ethical behavior? Provide a score (0-10).

    5. Visualize the Decision-Making Process:
       - Create a decision tree for each scenario to illustrate the decision-making process with if-else conditions.

    Example Prompt:  
    Should AI be used for grading exams?

    Example Response (JSON format):  
    [
        {{
            "scenario": "AI-driven exam grading is the scenario where artificial intelligence is used to evaluate and score student exams. This approach aims to enhance efficiency and consistency in grading by automating the process. However, it raises concerns about fairness, bias, and the ability to accurately assess subjective responses. The debate centers around whether the benefits of AI grading outweigh the potential drawbacks and ethical implications.",
            "key_actors": [
                {{"name": "Students", "role": "Receive grades"}},
                {{"name": "Teachers", "role": "Assign grades"}},
                {{"name": "Administrators", "role": "Oversee grading process"}}
            ],
            "risks": ["Bias", "Lack of human judgment", "Privacy concerns"],
            "benefits": ["Faster grading", "Reduced workload", "Standardized scoring"],
            "ethical_perspectives": {{
                "utilitarianism": {{"analysis": "Maximizes efficiency, potential bias.", "score": 7}},
                "deontology": {{"analysis": "Fairness, transparency.", "score": 6}},
                "virtue_ethics": {{"analysis": "Fairness, empathy.", "score": 8}}
            }},
            "decision_tree": {{
                "nodes": [
                    {{"id": 1, "label": "Start"}},
                    {{"id": 2, "label": "AI Grading"}},
                    {{"id": 3, "label": "Efficiency"}},
                    {{"id": 4, "label": "Bias"}},
                    {{"id": 5, "label": "Fairness"}}
                ],
                "edges": [
                    {{"from": 1, "to": 2}},
                    {{"from": 2, "to": 3, "condition": "If AI grading is efficient"}},
                    {{"from": 2, "to": 4, "condition": "If AI grading introduces bias"}},
                    {{"from": 4, "to": 5, "condition": "If bias is addressed"}}
                ]
            }}
        }},
        {{
            "scenario": "AI for employee productivity monitoring is the scenario where artificial intelligence is used to track and evaluate employee performance. This approach aims to enhance productivity and resource allocation by providing data-driven insights. However, it raises concerns about privacy, employee stress, and the potential misuse of data. The debate centers around whether the benefits of AI monitoring outweigh the potential drawbacks and ethical implications.",
            "key_actors": [
                {{"name": "Employees", "role": "Monitored for productivity"}},
                {{"name": "Management", "role": "Oversee productivity"}},
                {{"name": "AI Developers", "role": "Develop monitoring tools"}}
            ],
            "risks": ["Privacy invasion", "Employee stress", "Potential misuse of data"],
            "benefits": ["Increased productivity", "Better resource allocation", "Data-driven decision making"],
            "ethical_perspectives": {{
                "utilitarianism": {{"analysis": "Focuses on productivity, potential stress.", "score": 6}},
                "deontology": {{"analysis": "Privacy concerns, duty to respect rights.", "score": 5}},
                "virtue_ethics": {{"analysis": "Balance between productivity and well-being.", "score": 7}}
            }},
            "decision_tree": {{
                "nodes": [
                    {{"id": 1, "label": "Start"}},
                    {{"id": 2, "label": "AI Monitoring"}},
                    {{"id": 3, "label": "Productivity"}},
                    {{"id": 4, "label": "Privacy"}},
                    {{"id": 5, "label": "Well-being"}}
                ],
                "edges": [
                    {{"from": 1, "to": 2}},
                    {{"from": 2, "to": 3, "condition": "If AI monitoring increases productivity"}},
                    {{"from": 2, "to": 4, "condition": "If AI monitoring invades privacy"}},
                    {{"from": 4, "to": 5, "condition": "If privacy concerns are addressed"}}
                ]
            }}
        }}
    ]

    Prompt: 
    {prompt}
    """
    
    return generate_response(structured_prompt)

def generate_justification(prompt):
    structured_prompt = f"""
    Ethical Justification Generation

    AI must construct a structured ethical justification based on the given prompt.

    ### Instructions:

    1. Provide a Justification for the Decision:
       - Provide a detailed justification for the decision.
       - Clearly state why this decision is ethical.

    2. Analyze Pros and Cons:
       - List at least 3-4 pros.
       - List at least 3-4 cons.

    3. Counterarguments:
       - Provide at least three strong counterarguments against the decision.

    4. Summary of Findings:
       - Provide a structured summary (4-6 sentences) explaining the key ethical takeaways.
       - Ensure clarity and fairness in presenting the argument.

    5. Balanced Conclusion:
       - Provide a final reasoned conclusion weighing both sides.
       - Offer a well-balanced perspective on the ethical decision.

    Example Prompt:  
    Should AI be used for grading exams?

    Example Response (JSON format):  
    {{
        "summary": "AI-driven grading offers speed and consistency but raises concerns about fairness and bias. While automation enhances efficiency and reduces human workload, it may not fully capture the nuances of subjective answers. Ethical considerations include transparency, accountability, and fairness in evaluation. Institutions should implement oversight measures to mitigate risks. A hybrid approach, integrating AI with human assessment, could offer the best balance.",
        "justification": "AI grading ensures faster, fairer assessments but requires human oversight to prevent biases. By leveraging AI, educational institutions can streamline the grading process, reduce human error, and provide timely feedback to students. However, it is crucial to maintain human involvement to address subjective elements and ensure fairness.",
        "pros": ["Efficiency", "Standardization", "Scalability", "Reduced workload"],
        "cons": ["Bias in training data", "Lack of subjective assessment", "privacy concerns", "Over-reliance on automation"],
        "counterarguments": [
            "AI may reinforce biases present in historical data.",
            "It lacks human intuition for subjective responses.",
            "Over-reliance on AI may devalue teachers' roles in assessment."
        ],
        "conclusion": "While AI can improve grading efficiency, human oversight is necessary to ensure fairness and prevent biases. A hybrid model that leverages AI for objectivity while involving human review for subjective assessments would provide the most ethical and effective solution."
    }}

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
        "scenario": "AI-driven exam grading is the scenario where artificial intelligence is used to evaluate and score student exams. This approach aims to enhance efficiency and consistency in grading by automating the process. However, it raises concerns about fairness, bias, and the ability to accurately assess subjective responses. The debate centers around whether the benefits of AI grading outweigh the potential drawbacks and ethical implications.",
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

def generate_chat_response(message, chat_history):
    formatted_chat_history = "\n".join([f"{entry['role']}: {entry['content']}" for entry in chat_history])
    
    structured_prompt = f"""
    Continue the ethical debate based on the following chat history and the new message:

    Chat History:
    {formatted_chat_history}

    New Message: {message}

    Respond with a concise and relevant argument or counterargument.
    """
    print(chat_history)
    print(structured_prompt)
    
    response = generate_response(structured_prompt)
    print(response)
    try:
        response_json = json.loads(response)
        response_content = response_json["assistant"]  
    except ValueError:
        response_content = "Error: Invalid JSON response"
    
    return response_content