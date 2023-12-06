from flask import Flask, render_template, request
import random


app = Flask(__name__)

# Load word list from a file
with open('static/wordlist.txt', 'r') as file:
    word_list = [word.strip() for word in file.readlines() if word.strip()]

def get_random_word():
    return word_list[random.randint(0, len(word_list) - 1)]

def initialize_game():
    random_word = get_random_word()
    display_word = ['_'] * len(random_word)
    remaining_attempts = 6
    correct_letters_shown = set()
    incorrect_letters_shown = set()
    partial_letters_shown = set()

    return random_word, display_word, remaining_attempts, correct_letters_shown, incorrect_letters_shown, partial_letters_shown

@app.route('/')
def index():
    random_word, display_word, remaining_attempts, _, _, _ = initialize_game()
    return render_template('index.html', random_word=random_word, display_word=' '.join(display_word),
                           remaining_attempts=remaining_attempts, result='')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    random_word, display_word, remaining_attempts, correct_letters_shown, partial_letters_shown = \
        request.form['random_word'], list(request.form['display_word'].split()), int(request.form['remaining_attempts']), \
        set(request.form['correct_letters_shown']), set(request.form['partial_letters_shown'])

    guess = request.form['guess'].upper()
    result = ''

    if guess.isalpha() and len(guess) == 1:
        if guess in random_word:
            if guess not in correct_letters_shown:
                correct_letters_shown.add(guess)
                for i in range(len(random_word)):
                    if random_word[i] == guess:
                        display_word[i] = guess
            else:
                result = f"You already guessed '{guess}'. Try again."
        else:
            if guess not in partial_letters_shown and guess not in incorrect_letters_shown:
                partial_letters_shown.add(guess)
                remaining_attempts -= 1
            else:
                result = f"You already guessed '{guess}'. Try again."

        if all(char.isalpha() or char.isspace() for char in display_word):
            result = "Congratulations! You guessed the word!"
    else:
        result = "Invalid guess. Please enter a single letter."

    if remaining_attempts == 0 and not result:
        result = f"Sorry, you've run out of attempts. The correct word was {random_word}."

    return render_template('index.html', random_word=random_word, display_word=' '.join(display_word),
                           remaining_attempts=remaining_attempts, result=result,
                           correct_letters_shown=correct_letters_shown, partial_letters_shown=partial_letters_shown)


if __name__ == '__main__':
    app.run(debug=True)
