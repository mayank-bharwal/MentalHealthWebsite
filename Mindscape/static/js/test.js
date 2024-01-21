// Define the questions and their labels
const questions = [
    "In the past 4 weeks, about how often did you feel tired out for no good reason?",
    "In the past 4 weeks, about how often did you feel nervous?",
    "In the past 4 weeks, about how often did you feel so nervous that nothing could calm you down?",
    "In the past 4 weeks, about how often did you feel hopeless?",
    "In the past 4 weeks, about how often did you feel restless or fidgety?",
    "In the past 4 weeks, about how often did you feel so restless you could not sit still?",
    "In the past 4 weeks, about how often did you feel depressed?",
    "In the past 4 weeks, about how often did you feel that everything was an effort?",
    "In the past 4 weeks, about how often did you feel so sad that nothing could cheer you up?",
    "In the past 4 weeks, about how often did you feel worthless?"
];

// Function to generate the questions dynamically
function generateQuestions() {
    const questionsContainer = document.getElementById('questions-container');

    questions.forEach((question, index) => {
        const label = document.createElement('label');
        label.textContent = question;

        const radioContainer = document.createElement('div');

        for (let i = 5; i >= 1; i--) {
            const radioInput = document.createElement('input');
            radioInput.type = 'radio';
            radioInput.name = `question${index + 1}`;
            radioInput.value = i;
            radioContainer.appendChild(radioInput);

            const radioLabel = document.createElement('span');
            radioLabel.textContent = `(${i})`;
            radioContainer.appendChild(radioLabel);
        }

        questionsContainer.appendChild(label);
        questionsContainer.appendChild(radioContainer);
    });
}

// Call the function to generate the questions when the page loads
window.onload = generateQuestions;

function calculateScore(event) {
    event.preventDefault(); // Prevent default form submission
    let score = 0;

    // Calculate score
    for (let i = 1; i <= questions.length; i++) {
        const radios = document.getElementsByName('question' + i);
        for (const radio of radios) {
            if (radio.checked) {
                score += parseInt(radio.value, 10);
                break;
            }
        }
    }

    displayResults(score);
}

function displayResults(score) {
    const resultDiv = document.getElementById('result');
    let recommendation = '';
    
    if (score <= 19) {
        resultDiv.textContent = 'Likely to be well.';
        recommendation = 'Keep maintaining your mental health with positive activities like meditation and journaling.';
    } else if (score <= 24) {
        resultDiv.textContent = 'Likely to have a mild disorder.';
        recommendation = 'Consider daily journaling and mindfulness exercises. Listening to guided meditation can also be beneficial.';
    } else if (score <= 29) {
        resultDiv.textContent = 'Likely to have a moderate disorder.';
        recommendation = 'Regular journaling and guided meditation may help. It might also be helpful to talk to a professional counselor.';
    } else {
        resultDiv.textContent = 'Likely to have a severe disorder.';
        recommendation = 'It is important to seek professional counseling. Meanwhile, guided meditation and journaling can be supplementary aids.';
    }

    resultDiv.textContent += ' ' + recommendation;
    // Call a function to send this data to the server
    submitResults(score, recommendation);
}
function submitResults(score, recommendation) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit-test', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            window.location.href = '/dashboard'; // Redirect to dashboard immediately
        }
    };
    xhr.send(JSON.stringify({score: score, recommendation: recommendation}));
}


