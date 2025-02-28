document.addEventListener('DOMContentLoaded', function () {
    const storedPrompt = localStorage.getItem('prompt');
    if (storedPrompt) {
        console.log('Stored prompt:', storedPrompt);
        document.getElementById('promptInput').value = storedPrompt;
    }

    // Add click event listeners to feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
        card.addEventListener('click', function () {
            const gradient = this.getAttribute('data-gradient');
            const rect = this.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;

            const bloomEffect = document.getElementById('bloomEffect');
            bloomEffect.style.setProperty('--x', `${x}px`);
            bloomEffect.style.setProperty('--y', `${y}px`);
            bloomEffect.style.setProperty('--gradient', gradient);
            bloomEffect.style.background = gradient;
            bloomEffect.classList.add('active');

            // Display results after the animation
            setTimeout(() => {
                bloomEffect.classList.remove('active');
                bloomEffect.classList.add('stay');
                document.getElementById('results').classList.remove('d-none');

                // Load the content of insights.html for the first feature card
                if (index === 0) {
                    fetch('/insights')
                        .then(response => response.text())
                        .then(data => {
                            document.getElementById('resultsContent').innerHTML = data;
                        })
                        .catch(error => {
                            console.error('Error loading insights:', error);
                            document.getElementById('resultsContent').innerText = 'Error loading insights.';
                        });
                } else {
                    document.getElementById('resultsContent').innerText = 'Results displayed here...';
                }
            }, 1000);
        });
    });

    // Add click event listener to the back button
    document.getElementById('backButton').addEventListener('click', function () {
        document.getElementById('results').classList.add('d-none');
        document.getElementById('bloomEffect').classList.remove('stay');
    });
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