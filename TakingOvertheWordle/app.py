import random

from flask import Flask, render_template
from wordle_wordlist import get_word_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

word = "hello"
tries = 0 

@app.route('/wordle')
def wordle():
    guess = str(input(""))
    if guess == word:
        winner="you won"
    return render_template('wordle.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)

# Takes the guessed word, compares to secret word, returns True for valid guess, False or invalid
def top_level_checks(guess: str, secret_word: str) -> bool:
    if len(guess) != 5: return False
    if not guess.isalpha(): return False
    if guess.upper() not in get_word_list(): return False
    return True

# To Change...
# get_feedback("LEVER", "LOWER") --> "L--ER"
# get_feedback("MOMMY", "MADAM") --> "M-m--"
def get_feedback(guess: str, secret_word: str) -> str:
    guess = guess.lower()
    secret_word = secret_word.lower()
    word = secret_word

    # if the letter is in the right spot, make it uppercase
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
                guess = guess[: i] + "-" + guess[i+1:]
    return guess

def score():
    # score to equal tries it took to win over total games played 
    

    score = tries/games 