import random

from flask import Flask, render_template, request
from wordle_wordlist import get_word_list

app = Flask(__name__)

# Home route - Renders the title screen or handles form submission
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        player_name = request.form.get('player_name', 'Guest')
        return render_template('wordle.html', player_name=player_name)
    return render_template('index.html')

# Wordle route - Renders the play screen
@app.route('/wordle', methods=['POST'])
def wordle():
    player_name = request.form.get('player_name', 'Guest')
    return render_template('wordle.html', player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)

tries = 0 
gamesPlayed = 0 # add one everytime main function runs 

@app.route('/wordle')
def wordle():
    guess = request.form.get("guess")
    if guess == winWord:
        winner="you won"
    return render_template('wordle.html', winner=winner)

if __name__ == '__main__':
    # chooses random secret word from list
    winWord = random.choice(get_word_list())
    gamesPlayed += 1
    app.run(debug=True)

def play():
    while(guess != winWord or tries < 6):
        guess = str(input(""))
        #if not top_level_checks(guess, secret_word): break # subject to change
        tries+= 1 
        if guess == winWord:
            won = "you won"
            return render_template('index.html',won=won) # subject to change can y
        else: 
            get_feedback(guess)

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
    # Check for valid/invalid guesses before getting feedback
    guess = guess.lower()
    secret_word = secret_word.lower()

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

score = 0
def score():
    # score to equal tries it took to win over total games played 
    score = tries/gamesPlayed
    return score()
    
 