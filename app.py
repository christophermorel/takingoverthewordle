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
name = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global start_time, name
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('wordle', name=name))
    return render_template('index.html')

@app.route('/wordle', methods=['GET', 'POST'])
def wordle():
    global secret, guesses_data, checks_data, start_time, name
    
    if request.method == 'POST':
        # Extract the start_time from the form
        start_time_str = request.form.get('start_time', '0')
        name = request.form.get('name')
        
        # Check if start_time_str is not empty before converting to float
        if start_time_str:
            start_time = float(start_time_str)
        else:
            start_time = 0

        if start_time == 0:
            start_time = time.time()

        # Extract guesses
        if request.form.get('guess') is not None:
            guess = request.form.get('guess').upper()  # Assuming only one guess is submitted

            # Backend logic to create check data
            checks = create_check_data(secret, guess)

            # Append the current guess and checks to history
            guesses_data.append(guess)
            checks_data.append(checks)                    
            if checks == secret:
                elapsed_time = time.time() - start_time
                record_game_result(name, elapsed_time)

                # Reset the game
                secret = random.choice(get_word_list())
                guesses_data = []
                checks_data = []
                start_time = 0

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
            
    return render_template('wordle.html', rounds={'guesses': guesses_data, 'checks': checks_data, 'name': name, 'secret': secret, 'time': start_time})

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
