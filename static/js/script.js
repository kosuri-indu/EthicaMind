document.addEventListener('DOMContentLoaded', function () {
    const storedPrompt = localStorage.getItem('prompt');
    if (storedPrompt) {
        console.log('Stored prompt:', storedPrompt);
        document.getElementById('promptInput').value = storedPrompt;
    }
});

document.getElementById('promptForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const prompt = document.getElementById('promptInput').value;
    console.log('Prompt:', prompt);

    localStorage.setItem('prompt', prompt);
    console.log('Stored in local storage:', localStorage.getItem('prompt'));

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: prompt })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            document.getElementById('message').innerText = 'Prompt saved successfully!';
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('message').innerText = 'Error saving prompt.';
        });
});