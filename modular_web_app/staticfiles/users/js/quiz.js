document.addEventListener('DOMContentLoaded', function() {
    const topicSelect = document.getElementById('topic');
    const startQuizButton = document.getElementById('startQuiz');

    // Log to check if the script is running
    console.log('Quiz JS loaded');
    
    // Enable Start Quiz button when a topic is selected
    topicSelect.addEventListener('change', function() {
        console.log('Topic selected: ', topicSelect.value);
        if (topicSelect.value) {
            startQuizButton.disabled = false;
        } else {
            startQuizButton.disabled = true;
        }
    });

    // Redirect to quiz page when Start Quiz is clicked
    startQuizButton.addEventListener('click', function() {
        const topic = topicSelect.value;
        console.log('Starting quiz for topic: ', topic);
        if (topic) {
            window.location.href = `/quiz/${topic}/`;
        }
    });
});
