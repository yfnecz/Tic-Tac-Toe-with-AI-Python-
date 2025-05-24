# [Tic-Tac-Toe-with-AI-Python](https://tic-tac-toe-with-ai-python.onrender.com/)


An educational project with the Tic-Tac-Toe game.
There are 4 options: user, easy, medium and hard computer modes.

Deployed using render
# [Check it out](https://tic-tac-toe-with-ai-python.onrender.com/)

To run locally using docker

```
docker build -t tic-tac-toe .
```

```
docker run -p 5000:5000 tic-tac-toe
```

And open
http://127.0.0.1:5000/


In user mode, user chooses the cell.

On easy level, the computer just makes random moves.

When the AI is playing at medium difficulty level, it makes moves using the following logic:

1. If it already has two in a row and can win with one further move, it does so.
2. If its opponent can win with one move, it plays the move necessary to block this.
3. Otherwise, it makes a random move.

When the AI is playing at hard level, it uses [the minimax algorithm](https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/) to either win or get a draw.

It is possible to play user vs computer at any level, user vs user, or watch computer play against itself (on different or same levels).


