import random
import requests
from wordle_wordlist import get_word_list

# Returns random word from possible_words list
def cpu_guess(possible_words):
    return random.choice(possible_words)

# Function to get a random word from the Flask app
def get_winWord():
    response = requests.get('http://127.0.0.1:5000/get_winWord')
    data = response.json()
    return data['word']

# Returns a number, in string form, fron get_feedback()
def match_feedback(word, guess, feedback):
    return feedback == get_feedback(word, guess)

# Returns whether or not letter of each index in guess matches with secret word
def get_feedback(winWord, guess):
    feedback = ""

    # Iterates through length of secret word
    for i in range(len(winWord)):
        # Returns "1" if letter is in exact spot
        if guess[i] == winWord[i]:
            feedback += "1"
        # Returns "2" if letter is in wrong spot
        elif guess[i] in winWord:
            feedback += "2"
        # Returns "0" if letter not in word
        else:
            feedback += "0"
    return feedback

# Returns a list of new words that matches the new feedback
def process_feedback(possible_words, guess, feedback):
    return [word for word in possible_words if get_feedback(word, guess) == feedback]

# Runs the cpu when called
def cpu_wordle():

    # Chooses random word, forms a list of possible words, and tracks tries
    #winWord = random.choice(get_word_list()), to delete... in case does not work
    winWord = get_winWord()
    possible_words = get_word_list()
    max_tries = 5
    tries = 0

    # While cpu still has tries, keep guessing, to change when implementing into front-end (print statements)
    while tries < max_tries:
        guess = cpu_guess(possible_words)
        feedback = get_feedback(winWord,guess)

        print(f"Guess #{tries + 1}: {guess} | Feedback: {feedback}")

        if feedback == "11111":
            print(f"Congrats, the word was {winWord}, W!")
            break
        possible_words = process_feedback(possible_words, guess, feedback)
        tries += 1

    if feedback != "11111":
        print(f"GGs, better luck, right word is {winWord}!")

cpu_wordle()