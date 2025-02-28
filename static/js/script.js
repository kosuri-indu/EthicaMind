function analyzeEthics() {
    let question = document.getElementById("ethicalInput").value;

    if (!question) {
        alert("Please enter an ethical dilemma.");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        let output = `
            <h3>AI Response:</h3>
            <p><strong>Scenario:</strong> ${data.scenario}</p>
            <h4>Ethical Analysis:</h4>
            <ul>
                <li><strong>Utilitarianism:</strong> ${data.analysis.Utilitarianism}</li>
                <li><strong>Deontology:</strong> ${data.analysis.Deontology}</li>
                <li><strong>Virtue Ethics:</strong> ${data.analysis.Virtue_Ethics}</li>
            </ul>
        `;
        document.getElementById("output").innerHTML = output;
    })
    .catch(error => console.error("Error:", error));
}
