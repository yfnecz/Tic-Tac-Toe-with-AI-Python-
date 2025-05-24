from time import sleep

from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
from tictactoe import TicTacToe

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_game():
    if 'game' not in session:
        t = TicTacToe()
        t.init_game()
        session['game'] = t.game.tolist()
    else:
        t = TicTacToe()
        t.game = np.array(session['game'])
    return t

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'players' not in session:
        return redirect(url_for('select_players'))

    t = get_game()
    players = session['players']
    message = ''
    turn = session.get('turn', 0)

    if request.method == 'POST':
        move = request.form.get('move')
        if move:
            row, col = map(int, move.split(','))
            if t.game[row][col] == ' ':
                t.game[row][col] = 'X' if turn % 2 == 0 else 'O'
                session['game'] = t.game.tolist()
                turn += 1
                session['turn'] = turn
            else:
                message = 'Cell occupied!'

    result = t.count_winner()
    if result:
        message = result
        return render_template('index.html', game=t.game, message=message, players=players, turn=turn, auto_play=False)

    current_player = players[turn % 2]
    auto_play = False
    if current_player != 'user' and not message:
        # Computer's turn: make a move, then render with auto_play
        if current_player == 'easy':
            t.make_easy_move()
        elif current_player == 'medium':
            t.make_medium_move()
        elif current_player == 'hard':
            t.make_hard_move()
        session['game'] = t.game.tolist()
        session['turn'] = turn + 1
        auto_play = True  # Tell the template to auto-refresh

    return render_template('index.html', game=t.game, message=message, players=players, turn=turn, auto_play=auto_play)

@app.route('/select_players', methods=['GET', 'POST'])
def select_players():
    if request.method == 'POST':
        player1 = request.form['player1']
        player2 = request.form['player2']
        session['players'] = [player1, player2]
        session.pop('game', None)
        session['turn'] = 0
        return redirect(url_for('index'))
    return render_template('select_players.html')

@app.route('/reset')
def reset():
    session.pop('game', None)
    session.pop('players', None)
    session.pop('turn', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)