from flask import Flask, render_template, request, redirect, url_for
import random
from wordle_wordlist import get_word_list
from database import record_game_result
import time

app = Flask(__name__)

# Randomizes the secret word into secret
secret = random.choice(get_word_list())

# Initializing variables
guesses_data = []  # List to store history of guesses
checks_data = []   # List to store history of checks
start_time = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global start_time
    if request.method == 'POST':
        global name 
        name = request.form.get('name')
        
        if start_time is 0:
            start_time = time.time()

        return redirect(url_for('wordle', name=name))
    return render_template('index.html')

@app.route('/wordle', methods=['GET', 'POST'])
def wordle():
    global secret, guesses_data, checks_data  # Make these variables global


    if request.method == 'POST':

        name = request.form.get('name') 

        # Extract guesses
        if request.form.get('guess') != None:
            guess = (request.form.get('guess'))  # Assuming only one guess is submitted
            guess = guess.upper()

            # Backend logic to create check data
            checks = create_check_data(secret, guess)

            # Append the current guess and checks to history
            guesses_data.append(guess)
            checks_data.append(checks)

            if checks == secret:
                elapsed_time = int(time.time() - start_time)
                record_game_result(name, elapsed_time)

                # Reset the game
                secret = random.choice(get_word_list())
                guesses_data = []
                checks_data = []

                # Render template to user telling them they have won
                return render_template('game_over.html', message="Congratulations! You've won!")

            elif len(guesses_data) >= 6:
                elapsed_time = 0
                # Inform the player that they have lost and provide the correct word
                lost_message = f"Sorry, {name}! You have run out of guesses. The correct word was {secret}."
                secret = random.choice(get_word_list())
                guesses_data = []  # List to store history of guesses
                checks_data = []   # List to store history of checks
                start_time = 0
                return render_template('game_over.html', message=lost_message)
                
            
    return render_template('wordle.html', rounds={'guesses': guesses_data, 'checks': checks_data, 'name': name, 'secret': secret})

def create_check_data(secret, guess):
    guess = guess.lower()
    secret_word = secret.lower()
    word = secret_word

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            guess = guess[0:i] + guess[i].upper() + guess[i + 1 :]
            word_i = word.find(secret_word[i])
            word = word[0:word_i] + word[word_i + 1 :]

    for i in range(len(guess)):
        if guess[i].islower():
            if guess[i] in word:
                word_i = word.find(guess[i])
                if word_i == len(word) - 1:
                    word = word[0:word_i]
                else:
                    word = word[0:word_i] + word[word_i + 1 :]
            else:
                guess = guess[:i] + "-" + guess[i + 1 :]
    return guess

if __name__ == '__main__':
    app.run(debug=True)



'''
- Correct letter, correct spot: uppercase letter
- Correct letter, wrong spot: lowercase letter
- Letter not in the word: '-'
For example:
    - create_check_data("lever", "EATEN") --> "-e-E-"
    - create_check_data("LEVER", "LOWER") --> "L--ER"
    - create_check_data("MOMMY", "MADAM") --> "M-m--"
    - create_check_data("ARGUE", "MOTTO") --> "-----"
'''