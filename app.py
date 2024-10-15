from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

import wordlist

# Younger Futhark runes (16 characters)
RUNES = "ᚠᚢᚦᚬᚱᚴᚼᚾᛁᛅᛋᛏᛒᛘᛚᛦ"

# Sample database of 5-letter Old Norse words (you would need to populate this with actual words)
WORDS = wordlist.runic_words

# Choose a random word for the game
target_word = random.choice(WORDS)
print(target_word)

@app.route('/')
def index():
    return render_template('index.html', runes=RUNES)


@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json['guess']

    if len(guess) != 5:
        return jsonify({'error': 'Guess must be 5 characters long'}), 400

    result = [''] * 5
    for i in range(5):
        if guess[i] == target_word[i]:
            result[i] = 'green'
        elif guess[i] in target_word:
            result[i] = 'yellow'
        else:
            result[i] = 'grey'

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
