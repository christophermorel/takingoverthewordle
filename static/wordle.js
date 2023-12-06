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
    let incorrectLettersShown = new Set();
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

            if (wordList.includes(guess)) {
                if (guess.length === randomWord.length) {
                    let correctLetters = 0;

                    for (let i = 0; i < randomWord.length; i++) {
                        if (i < guess.length && guess[i] === randomWord[i]) {
                            correctLetters++;
                            if (!correctLettersShown.has(randomWord[i])) {
                                displayWord[i] = `<span class="correct">${randomWord[i]}</span>`;
                                correctLettersShown.add(randomWord[i]);
                            }
                        } else if (randomWord.includes(guess[i]) && randomWord.indexOf(guess[i]) !== i) {
                            if (!partialLettersShown.has(guess[i]) && !correctLettersShown.has(guess[i])) {
                                displayWord[i] = `<span class="partial">${guess[i]}</span>`;
                                partialLettersShown.add(guess[i]);
                            }
                        }
                    }

                    console.log("Display Word:", displayWord.join(" "));

                    wordDisplay.innerHTML = displayWord.join(" ");

                    if (correctLetters === randomWord.length) {
                        resultDisplay.innerHTML = "Congratulations! You guessed the word!";
                        guessHistory.push(`<div class="correct">${randomWord}</div>`); // Display only the correct word in the history with correct class
                        guessHistoryDisplay.innerHTML = guessHistory.join("");
                        guessInput.disabled = true;
                    } else {
                        resultDisplay.innerHTML = `Incorrect guess. ${remainingAttempts} attempts remaining.`;
                        remainingAttempts--;

                        if (remainingAttempts === 0) {
                            resultDisplay.innerHTML = `Sorry, you've run out of attempts. The correct word was ${randomWord}.`;
                            guessInput.disabled = true;
                        }

                        // Replace underscores with incorrect letters in the display
                        for (let i = 0; i < randomWord.length; i++) {
                            if (!correctLettersShown.has(randomWord[i]) && !partialLettersShown.has(randomWord[i])) {
                                displayWord[i] = `<span class="incorrect">${randomWord[i]}</span>`;
                                incorrectLettersShown.add(randomWord[i]);
                            }
                        }

                        // Update the displayed word
                        wordDisplay.innerHTML = displayWord.join(" ");

                        const guessHistoryEntry = displayWord.map(char => char.includes('span') ? char : '_').join(" ");
                        guessHistory.push(`<div>${guessHistoryEntry}</div>`);
                        guessHistoryDisplay.innerHTML = guessHistory.join("");

                        correctLettersShown.clear();
                        partialLettersShown.clear();
                    }
                } else {
                    resultDisplay.innerHTML = "Please enter a word with the correct number of letters.";
                }
            } else {
                resultDisplay.innerHTML = "Invalid guess. Please enter a valid word from the word list.";

                // Replace underscores with incorrect letters in the display
                for (let i = 0; i < randomWord.length; i++) {
                    if (!correctLettersShown.has(randomWord[i]) && !partialLettersShown.has(randomWord[i])) {
                        displayWord[i] = `<span class="incorrect">${randomWord[i]}</span>`;
                        incorrectLettersShown.add(randomWord[i]);
                    }
                }

                // Update the displayed word
                wordDisplay.innerHTML = displayWord.join(" ");

                if (guess.length === 1 && !incorrectLettersShown.has(guess)) {
                    incorrectLettersShown.add(guess);
                }

                const guessHistoryEntry = displayWord.map(char => char.includes('span') ? char : '_').join(" ");
                guessHistory.push(`<div>${guessHistoryEntry}</div>`);
                guessHistoryDisplay.innerHTML = guessHistory.join("");
            }

            guessInput.value = "";
        };
    }
});