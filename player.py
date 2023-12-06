import random
from wordle_wordlist import get_word_list

def player_guess():
    guess = str(input("guess"))
    return(guess)

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
    return [word for word in possible_words if get_feedback(word, guess) == feedback]

def cpu_wordle():
    winWord = random.choice(get_word_list())
    possible_words = get_word_list()
    max_tries = 5
    tries = 0

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