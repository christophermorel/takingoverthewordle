import random
from wordle_wordlist import get_word_list
from app import get_winWord

def player_guess():
    guess = str(input("guess"))
    guess = guess.upper()
    return(guess)

def match_feedback(word, guess, feedback):
    return feedback == get_feedback(word, guess)

def get_feedback(winWord, guess):
    guess = guess.lower()
    secret_word = winWord.lower()
    word = secret_word
        
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            guess = guess[0: i] + guess[i].upper() + guess[i+1:]
            word_i = word.find(secret_word[i])
            word = word[0: word_i] + word[word_i+1:]

    for i in range(len(guess)):
        if guess[i].islower(): 
            if guess[i] in word:
                word_i = word.find(guess[i])
                if word_i == len(word)-1:
                    word = word[0: word_i]
                else:
                    word = word[0: word_i] + word[word_i+1:]
            else:
                guess = guess[: i] + "_" + guess[i+1:]
    return guess

def process_feedback(possible_words, guess, feedback):
    return [word for word in possible_words if get_feedback(word, guess) == feedback]

def player_wordle():
    winWord = get_winWord()
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