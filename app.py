from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
app.jinja_env.filters['sum'] = sum
app.jinja_env.filters['len'] = len
app.secret_key = os.urandom(24)

# Configure the Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './sessions'
Session(app)

def init_session():
    session['players'] = []
    session['rounds'] = []
    session['dealer'] = None

@app.route('/')
def index():
    if 'players' not in session:
        init_session()
    return render_template('index.html', game_data=session)

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    if not player_name:
        flash('Player name cannot be blank.')
        return redirect(url_for('index'))
    if not session['players']:
        session['players'] = []
        session['rounds'] = [[] for _ in range(len(session['players']))]
        session['dealer'] = 0
    session['players'].append(player_name)
    session['rounds'].append([])
    return redirect(url_for('index'))

@app.route('/new_round', methods=['POST'])
def new_round():
    if not session['players']:
        flash("Please add players before adding a new round.")
        return redirect(url_for('index'))

    scores = request.form.getlist('scores[]')

    for i, score in enumerate(scores):
        session['rounds'][i].append(int(score))

    session['dealer'] = (session['dealer'] + 1) % len(session['players'])

    # Check for a winner
    for player, round_scores in zip(session['players'], session['rounds']):
        if sum(round_scores) >= 100:
            flash(f'{player} has gone over and finished the game with a score of {sum(round_scores)}!')
            break

    return redirect(url_for('index'))

@app.route('/new_game', methods=['POST'])
def new_game():
    init_session()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
