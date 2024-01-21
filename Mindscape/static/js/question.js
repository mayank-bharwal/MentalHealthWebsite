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
