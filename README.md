# Tic-Tac-Toe-with-AI-Python-


An educational project with the Tic-Tac-Toe game.
There are 4 options: user, easy, medium and hard computer modes.

In user mode, user enters the coordinates.

On easy level, the computer just makes random moves.

When the AI is playing at medium difficulty level, it makes moves using the following logic:

1. If it already has two in a row and can win with one further move, it does so.
2. If its opponent can win with one move, it plays the move necessary to block this.
3. Otherwise, it makes a random move.

When the AI is playing at hard level, it uses [the minimax algorithm](https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/) to either win or get a draw.

It is possible to play user vs computer at any level, user vs user, or watch computer play against itself (on different or same levels).

Example 1

```
Input command: > start hard user
Making move level "hard"
---------
|       |
| X     |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
| X O   |
|       |
---------
Making move level "hard"
---------
|   X   |
| X O   |
|       |
---------
Enter the coordinates: > 3 2
---------
|   X   |
| X O   |
|   O   |
---------
Making move level "hard"
---------
| X X   |
| X O   |
|   O   |
---------
Enter the coordinates: > 3 1
---------
| X X   |
| X O   |
| O O   |
---------
Making move level "hard"
---------
| X X X |
| X O   |
| O O   |
---------
X wins

Input command: > exit
```

Example 2

```
Input command: start hard hard
---------
|       |
|       |
|       |
---------
Making move level "hard"
---------
|       |
|       |
|   X   |
---------
Making move level "hard"
---------
|   O   |
|       |
|   X   |
---------
Making move level "hard"
---------
| X O   |
|       |
|   X   |
---------
Making move level "hard"
---------
| X O   |
|       |
| O X   |
---------
Making move level "hard"
---------
| X O X |
|       |
| O X   |
---------
Making move level "hard"
---------
| X O X |
|   O   |
| O X   |
---------
Making move level "hard"
---------
| X O X |
| X O   |
| O X   |
---------
Making move level "hard"
---------
| X O X |
| X O O |
| O X   |
---------
Making move level "hard"
---------
| X O X |
| X O O |
| O X X |
---------
Draw
Input command: exit
```
