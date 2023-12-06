import random


def make_guess(possible_words):
    # Choose a guess that maximizes information gain
    return possible_words[len(possible_words) // 2]

def get_feedback(secret_word, guess):
    # Compare the secret word and the guess
    # Return feedback in the form of green, yellow, and gray pegs
    feedback = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback += "G"  # Correct letter in the correct position
        elif guess[i] in secret_word:
            feedback += "Y"  # Correct letter in the wrong position
        else:
            feedback += "X"  # Incorrect letter
    return feedback

def refine_guesses(possible_words, guess, feedback):
    # Refine the list of possible words based on the feedback
    # Eliminate words that don't match the feedback
    return [word for word in possible_words if get_feedback(word, guess) == feedback]

def play_wordle():
    secret_word = random.choice(get_word_list())
    possible_words = get_word_list()
    max_tries = 5
    tries = 0

    while tries < max_tries:
        guess = make_guess(possible_words)
        feedback = get_feedback(secret_word, guess)

        print(f"Guess #{tries + 1}: {guess} | Feedback: {feedback}")

        if feedback == "GGGGG":
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        possible_words = refine_guesses(possible_words, guess, feedback)
        tries += 1

    if feedback != "GGGGG":
        print(f"Sorry, you couldn't guess the word. The correct word was: {secret_word}")

# Run the game
play_wordle()







import random

def make_guess(possible_words):
    # Randomly select a word from the list of possible words
    return random.choice(possible_words)

def match_feedback(word, guess, feedback):
    # Check if the feedback matches between the word and the guess
    return feedback == get_feedback(word, guess)

def get_feedback(word, guess):
    # Generate feedback for the given word and guess
    return [1 if word[i] == guess[i] else 0 for i in range(min(len(word), len(guess)))]

def process_feedback(possible_words, guess, feedback):
    # Update the list of possible words based on the feedback
    return [word for word in possible_words if match_feedback(word, guess, feedback)]

# Example usage
word_list = ["apple", "table", "chair", "laser", "world", "python", "coding", "guess", "happy"]
possible_words = word_list.copy()

# Play the game with a limit of 5 guesses
target_word = random.choice(word_list)
max_guesses = 5

for attempt in range(1, max_guesses + 1):
    guess = make_guess(possible_words)
    feedback = get_feedback(target_word, guess)

    print(f"Attempt {attempt}: Guess: {guess}, Feedback: {feedback}")

    if guess == target_word:
        print("Congratulations! You guessed the word.")
        break

    possible_words = process_feedback(possible_words, guess, feedback)

    if attempt == max_guesses:
        print(f"Sorry, you've reached the maximum number of guesses. The word was {target_word}.")


"""
import random

def cpu_guess(possible_words):

    return random.choice(possible_words)

def match_feedback(word, guess, feedback):
    return feedback == get_feedback(word, guess)

def get_feedback(winWord, guess):
    feedback = ""

    for i in range(len(winWord)):
        if guess[i] == winWord[i]:
            feedback += "1"
        elif guess[i] in winWord:
            feedback += "2"
        else:
            feedback += "0"
    return feedback

def process_feedback(possible_words, guess, feedback):
    return [word for word in possible_words if match_feedback(word, guess) == feedback]

def cpu_wordle():
    winWord = random.choice(get_word_list())
    possible_words = get_word_list()
    max_tries = 5
    tries = 0

    while tries < max_tries:
        guess = cpu_guess(possible_words)
        feedback = get_feedback(winWord)

        print(f"Guess #{tries + 1}: {guess} | Feedback: {feedback}")

        if feedback == "11111":
            print(f"Congrats, the word was {winWord}, W!")
            break
        possible_words = process_feedback(possible_words, guess, feedback)
        tries += 1

    if feedback != "11111":
        print(f"GGs, better luck, right word is {winWord}!")

cpu_wordle()
"""