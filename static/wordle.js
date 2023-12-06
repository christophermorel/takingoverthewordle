document.addEventListener("DOMContentLoaded", function () {
    const wordDisplay = document.getElementById("word-display");
    const resultDisplay = document.getElementById("result");
    const guessHistoryContainer = document.getElementById("guess-history-container");
    const guessHistoryDisplay = document.getElementById("guess-history");
    const guessInput = document.getElementById("guess");
    let remainingAttempts = 6;
    let wordList;
    let guessHistory = [];
    let correctLettersShown = new Set();
    let partialLettersShown = new Set();

    // Load word list from a file
    fetch('/static/wordlist.txt')
        .then(response => response.text())
        .then(data => {
            wordList = data.split('\n').map(word => word.trim()).filter(word => word.length > 0);
            startGame();
        })
        .catch(error => console.error('Error loading word list:', error));

    function getRandomWord(wordList) {
        return wordList[Math.floor(Math.random() * wordList.length)];
    }

    function startGame() {
        const randomWord = getRandomWord(wordList);
        let displayWord = Array.from({ length: randomWord.length }, () => "_");
        wordDisplay.innerHTML = displayWord.join(" ");

        console.log("Random Word:", randomWord);

        window.submitGuess = function () {
            const guess = guessInput.value.toUpperCase();

            console.log("Player Guess:", guess);

            if (guess.length > 0) {
                let correctLetters = 0;

                for (let i = 0; i < randomWord.length; i++) {
                    if (i < guess.length && guess[i] === randomWord[i]) {
                        correctLetters++;
                        if (!correctLettersShown.has(guess[i])) {
                            displayWord[i] = `<span class="correct">${randomWord[i]}</span>`;
                            correctLettersShown.add(guess[i]);
                        }
                    } else if (randomWord.includes(guess[i]) && randomWord.indexOf(guess[i]) !== i) {
                        // Check if the guessed letter is not in the correct position
                        if (!partialLettersShown.has(guess[i])) {
                            displayWord[i] = `<span class="partial">${guess[i]}</span>`;
                            partialLettersShown.add(guess[i]);
                        }
                    }
                }

                console.log("Display Word:", displayWord.join(" "));

                wordDisplay.innerHTML = displayWord.join(" ");

                if (correctLetters === randomWord.length) {
                    resultDisplay.innerHTML = "Congratulations! You guessed the word!";
                    guessInput.disabled = true;
                } else {
                    resultDisplay.innerHTML = `Incorrect guess. ${remainingAttempts} attempts remaining.`;
                    remainingAttempts--;

                    if (remainingAttempts === 0) {
                        resultDisplay.innerHTML = `Sorry, you've run out of attempts. The correct word was ${randomWord}.`;
                        guessInput.disabled = true;
                    }

                    // Add only placeholders, correct, and partial guesses to the guess history
                    const guessHistoryEntry = displayWord.map(char => char.includes('span') ? char : '_').join(" ");
                    guessHistory.push(`<div>${guessHistoryEntry}</div>`);
                    guessHistoryDisplay.innerHTML = guessHistory.join("");

                    // Reset the sets of correct and partial letters shown for the next guess
                    correctLettersShown.clear();
                    partialLettersShown.clear();
                }
            } else {
                resultDisplay.innerHTML = "Please enter a word.";
            }

            guessInput.value = "";
        };
    }
});