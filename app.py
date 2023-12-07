from flask import Flask, render_template, request, redirect, url_for
import random
from wordle_wordlist import get_word_list

app = Flask(__name__)

# Initializing variables
guesses_data = []  # List to store history of guesses
checks_data = []   # List to store history of checks

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('wordle', name=name))
    return render_template('index.html')

@app.route('/wordle', methods=['GET', 'POST'])
def wordle():

    if request.method == 'POST':
        
        # Randomizes the secret word into secret
        secret = random.choice(get_word_list())

        name = request.form.get('name')  # Extract the 'name' from the form data

        # Extract guesses
        if request.form.get('guess') != None:
            guess = (request.form.get('guess'))  # Assuming only one guess is submitted
            guess = guess.upper()

            # Backend logic to create check data
            checks = create_check_data(secret, guess)

            # Append the current guess and checks to history
            guesses_data.append(guess)
            checks_data.append(checks)

    return render_template('wordle.html', rounds={'guesses': guesses_data, 'checks': checks_data, 'name': name, 'secret': secret})

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
                guess = guess[:i] + "_" + guess[i + 1 :]
    return guess

if __name__ == '__main__':
    app.run(debug=True)
