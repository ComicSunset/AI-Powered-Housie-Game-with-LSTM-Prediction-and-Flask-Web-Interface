from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Generate random Housie card
def generate_card():
    card = []
    for _ in range(3):
        row = random.sample(range(1, 91), 5)
        card.append(sorted(row))
    return card

# Mark the number on the card
def mark_number(card, number):
    for row in card:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = 0  # Mark the number as 0 (marked)

# Check if a player has completed a line (row)
def check_line(row):
    return all(num == 0 for num in row)

# Check if there's a winner (if all three rows are marked)
def check_winner(card):
    return all(check_line(row) for row in card)

# Initializing the game
player1_card = generate_card()
player2_card = generate_card()
numbers_called = []

@app.route('/')
def index():
    return render_template('index.html', player1_card=player1_card, player2_card=player2_card)

@app.route('/call_number')
def call_number():
    number = random.randint(1, 90)
    numbers_called.append(number)
    mark_number(player1_card, number)
    mark_number(player2_card, number)

    # Check for winners
    winner = None
    if check_winner(player1_card):
        winner = 'Player 1 wins!'
    elif check_winner(player2_card):
        winner = 'Player 2 wins!'

    return jsonify({'number': number, 'player1_card': player1_card, 'player2_card': player2_card, 'winner': winner})

if __name__ == '__main__':
    app.run(debug=True)
