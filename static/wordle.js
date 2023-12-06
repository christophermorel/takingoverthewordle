document.addEventListener("DOMContentLoaded", function () {
    const wordDisplay = document.getElementById("word-display");
    const resultDisplay = document.getElementById("result");
    let remainingAttempts = 6;
    let wordList;

    // Load word list from a file
    fetch('/static/wordlist.txt')
        .then(response => response.text())
        .then(data => {
            wordList = data.split('\n').map(word => word.trim()).filter(word => word.length > 0);
            startGame();
        })
        .catch(error => console.error('Error loading word list:', error));

    // Function to get a random word from the list
    function getRandomWord(wordList) {
        return wordList[Math.floor(Math.random() * wordList.length)];
    }

    // Function to start the game
    function startGame() {
        const randomWord = getRandomWord(wordList);

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
                    } else if (randomWord.includes(guess[i])) {
                        displayWord[i] = `<span class="partial">${guess[i]}</span>`;
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
    }
});