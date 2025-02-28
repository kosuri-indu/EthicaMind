document.addEventListener('DOMContentLoaded', function () {
    const storedPrompt = localStorage.getItem('prompt');
    if (storedPrompt) {
        console.log('Stored prompt:', storedPrompt);
        document.getElementById('promptInput').value = storedPrompt;
    }

    // Add click event listeners to feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
        card.addEventListener('click', function () {
            const imgSrc = this.querySelector('img').src;
            const rect = this.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;

            const bloomEffect = document.getElementById('bloomEffect');
            bloomEffect.style.setProperty('--x', `${x}px`);
            bloomEffect.style.setProperty('--y', `${y}px`);
            bloomEffect.style.backgroundImage = `url(${imgSrc})`;
            bloomEffect.classList.add('active');

            // Store the image source in local storage
            localStorage.setItem('backgroundImage', imgSrc);

            // Determine the target page based on the feature card index
            let targetPage = '/insights';
            if (index === 1) {
                targetPage = '/scenarios';
            } else if (index === 2) {
                targetPage = '/debate';
            } else if (index === 3) {
                targetPage = '/justification';
            }

            // Navigate to the target page after the bloom effect
            setTimeout(() => {
                window.location.href = targetPage;
            }, 1000);
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

    // Apply fade-in effect to the body
    document.body.classList.add('fade-in');
});