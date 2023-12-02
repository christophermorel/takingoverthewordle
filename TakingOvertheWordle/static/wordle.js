document.addEventListener("DOMContentLoaded", function () {
    const wordList = ["apple", "banana", "cherry", "grape", "lemon", "orange", "peach", "plum", "melon"];

    const randomWord = wordList[Math.floor(Math.random() * wordList.length)];
    const wordDisplay = document.getElementById("word-display");
    const resultDisplay = document.getElementById("result");
    let remainingAttempts = 6;

    // Display placeholders for the word
    const displayWord = Array.from({ length: randomWord.length }, () => "_");
    wordDisplay.innerHTML = displayWord.join(" ");

    // Function to handle the player's guess
    window.submitGuess = function () {
        const guessInput = document.getElementById("guess");
        const guess = guessInput.value.toLowerCase();

        if (guess.length > 0) {
            let correctLetters = 0;

            // Check if the guess matches the word
            for (let i = 0; i < randomWord.length; i++) {
                if (i < guess.length && guess[i] === randomWord[i]) {
                    correctLetters++;
                    displayWord[i] = `<span class="correct">${randomWord[i]}</span>`;
                } else {
                    displayWord[i] = "_";
                }
            }

            // Update the displayed word
            wordDisplay.innerHTML = displayWord.join(" ");

            // Check if the player guessed the entire word
            if (correctLetters === randomWord.length) {
                resultDisplay.innerHTML = "Congratulations! You guessed the word!";
            } else {
                resultDisplay.innerHTML = `Incorrect guess. ${remainingAttempts} attempts remaining.`;
                remainingAttempts--;

                if (remainingAttempts === 0) {
                    resultDisplay.innerHTML = `Sorry, you've run out of attempts. The correct word was ${randomWord}.`;
                    guessInput.disabled = true;
                }
            }
        } else {
            resultDisplay.innerHTML = "Please enter a word.";
        }

        guessInput.value = ""; // Clear the input field
    };
});
