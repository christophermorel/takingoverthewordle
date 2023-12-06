import random
from wordle_wordlist import get_word_list

def player_guess():
    guess = str(input("guess"))
    guess = guess.upper()
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

def player_wordle():
    winWord = random.choice(get_word_list())
    max_tries = 5
    tries = 0

    while tries < max_tries:
        
        new_word = str(input(""))
        new_word = new_word.upper()
        feedback = get_feedback(winWord,new_word)

        print(f"Guess #{tries + 1}: {new_word} | Feedback: {feedback}")

        if feedback == "11111":
            print(f"Congrats, the word was {new_word}, W!")
            break
        tries += 1

    if feedback != "11111":
        print(f"GGs, better luck, right word is {winWord}!")

player_wordle()