document.addEventListener("DOMContentLoaded", function () {
    const wordList = ["apple", "banana", "cherry", "grape", "lemon", "orange", "peach", "plum", "melon"];

    const randomWord = wordList[Math.floor(Math.random() * wordList.length)];
    const wordDisplay = document.getElementById("word-display");
    const resultDisplay = document.getElementById("result");
    let remainingAttempts = 6;

    // Display placeholders for the word
    const displayWord = Array.from({ length: randomWord.length }, () => "_").join(" ");
    wordDisplay.textContent = displayWord;

    // Function to handle the player's guess
    window.submitGuess = function () {
        const guessInput = document.getElementById("guess");
        const guess = guessInput.value.toLowerCase();

        if (guess.length === 5) {
            // Check if the guess matches the word
            if (guess === randomWord) {
                resultDisplay.textContent = "Congratulations! You guessed the word!";
            } else {
                resultDisplay.textContent = `Incorrect guess. ${remainingAttempts} attempts remaining.`;
                remainingAttempts--;

                if (remainingAttempts === 0) {
                    resultDisplay.textContent = `Sorry, you've run out of attempts. The correct word was ${randomWord}.`;
                    guessInput.disabled = true;
                }
            }
        } else {
            resultDisplay.textContent = "Please enter a five-letter word.";
        }

        guessInput.value = ""; // Clear the input field
    };
});
