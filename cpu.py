import random
from wordle_wordlist import get_word_list

# Returns random word from possible_words list
def cpu_guess(possible_words):
    return random.choice(possible_words)

# Returns a number, in string form, fron get_feedback()
def match_feedback(word, guess, feedback):
    return feedback == get_feedback(word, guess)

# Returns whether or not letter of each index in guess matches with secret word
def get_feedback(secretWord, guess):
    feedback = ""

    # Iterates through length of secret word
    for i in range(len(secretWord)):
        # Returns "1" if letter is in exact spot
        if guess[i] == secretWord[i]:
            feedback += "1"
        # Returns "2" if letter is in wrong spot
        elif guess[i] in secretWord:
            feedback += "2"
        # Returns "0" if letter not in word
        else:
            feedback += "0"
    return feedback

# Returns a list of new words that matches the new feedback
def process_feedback(possible_words, guess, feedback):
    return [word for word in possible_words if get_feedback(word, guess) == feedback]

# Runs the cpu when called
def cpu_wordle(secretWord):
    # find how to import secret_word from app.py or transfer this logic there 

    # Chooses random word, forms a list of possible words, and tracks tries
    #secretWord = random.choice(get_word_list()), to delete... in case does not work
    possible_words = get_word_list()
    max_tries = 5
    tries = 0

    # While cpu still has tries, keep guessing, to change when implementing into front-end (print statements)
    while tries < max_tries:
        guess = cpu_guess(possible_words)
        feedback = get_feedback(secretWord,guess)

        if feedback == "11111":
            return tries

        possible_words = process_feedback(possible_words, guess, feedback)
        tries += 1

    if feedback != "11111":
        return 0