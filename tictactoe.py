import numpy as np
from random import choice


class TicTacToe:
    def __init__(self):
        self.game = None

    def init_game(self):
        self.game = np.empty((3, 3), dtype=str)
        self.game.fill(' ')

    def print_game(self):
        print('---------')
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                print(self.game[i][j], end=' ')
            print('|')
        print('---------')

    def count_winner(self, game=None):
        if game is None:
            game = self.game
        result = None
        for i in range(2):
            if 3 in np.count_nonzero(game == 'X', axis=i):
                result = 'X wins'
                break
            elif 3 in np.count_nonzero(game == 'O', axis=i):
                result = 'O wins'
                break
        if not result:
            if game[0][0] == game[1][1] == game[2][2] and game[0][0] != ' ':
                result = game[0][0] + ' wins'
            elif game[2][0] == game[1][1] == game[0][2] and game[1][1] != ' ':
                result = game[1][1] + ' wins'
            elif not np.count_nonzero(game == ' '):
                result = 'Draw'
        return result

    def get_free_cells(self, game=None):
        if game is None:
            game = self.game
        return [(i, j) for i, x in enumerate(game) for j, y in enumerate(x) if y == ' ']

    def make_easy_move_helper(self):
        free_cells = self.get_free_cells()
        move = choice(free_cells)
        if np.count_nonzero(self.game == 'X') == np.count_nonzero(self.game == 'O'):
            self.game[move[0]][move[1]] = 'X'
        else:
            self.game[move[0]][move[1]] = 'O'

    def make_easy_move(self):
        print('Making move level "easy"')
        self.make_easy_move_helper()
        self.print_game()

    def make_medium_move(self):
        print('Making move level "medium"')
        if np.count_nonzero(self.game == ' ') > 8:
            self.make_easy_move_helper()  # random move on empty board
        else:
            playing = []
            if np.count_nonzero(self.game == 'X') == np.count_nonzero(self.game == 'O'):
                playing = ['X', 'O']
            else:
                playing = ['O', 'X']
            free_cells = self.get_free_cells()
            found = False
            opponent_cells = []
            for cell in free_cells:
                new_game = np.copy(self.game)
                new_game[cell[0]][cell[1]] = playing[0]
                if self.count_winner(game=new_game) == playing[0] + ' wins':
                    self.game[cell[0]][cell[1]] = playing[0]
                    found = True
                    break
                else:
                    new_game[cell[0]][cell[1]] = playing[1]
                    if self.count_winner(game=new_game) == playing[1] + ' wins':
                        opponent_cells.append(cell)
            if not found:
                if len(opponent_cells):
                    cell = choice(opponent_cells)
                    self.game[cell[0]][cell[1]] = playing[0]
                else:
                    move = choice(free_cells)
                    self.game[move[0]][move[1]] = playing[0]
        self.print_game()

    def minimax(self, player, minmax, game, cell):
        new_game = np.copy(game)
        new_game[cell[0]][cell[1]] = player
        result = self.count_winner(game=new_game)
        if result:
            if result == 'Draw':
                return 0
            elif 'wins' in result:
                if result == player + ' wins':
                    if minmax:  # player who is playing to win has won
                        return 10
                    else:  # player who is playing to lose has won
                        return -10
                else:  # the other player won
                    if minmax:
                        return -10
                    else:
                        return 10
        else:  # game not finished
            free_cells = self.get_free_cells(new_game)
            scores = []
            new_player = 'X'
            if player == 'X':
                new_player = 'O'
            for new_cell in free_cells:
                score = self.minimax(new_player, not minmax, new_game, new_cell)
                scores.append(score)
            if minmax:
                return min(scores)
            else:
                return max(scores)

    def make_hard_move(self):
        print('Making move level "hard"')
        if np.count_nonzero(self.game == ' ') > 8:
            self.make_easy_move_helper()  # random move on empty board
        else:
            if np.count_nonzero(self.game == 'X') == np.count_nonzero(self.game == 'O'):
                playing = ['X', 'O']
            else:
                playing = ['O', 'X']
            free_cells = self.get_free_cells()
            scores = dict()
            for cell in free_cells:
                scores[(cell[0], cell[1])] = self.minimax(playing[0], True, self.game, cell)
            move = sorted(scores.items(), key=lambda v: v[1], reverse=True)[0][0]
            self.game[move[0]][move[1]] = playing[0]
        self.print_game()

    def input_coordinates(self):
        coord = input("Enter the coordinates: ").split()
        result = None
        for i in range(2):
            if not coord[i].isdigit():
                print("You should enter numbers!")
                break
            elif int(coord[i]) < 1 or int(coord[i]) > 3:
                print("Coordinates should be from 1 to 3!")
                break
        else:
            coord = [int(x) - 1 for x in coord]
            if self.game[coord[0]][coord[1]] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                result = coord
        return result

    def human_move(self):
        result = False
        while not result:
            coord = self.input_coordinates()
            if coord:
                result = True
                if np.count_nonzero(self.game == 'X') == np.count_nonzero(self.game == 'O'):
                    self.game[coord[0]][coord[1]] = 'X'
                else:
                    self.game[coord[0]][coord[1]] = 'O'
                self.print_game()

    @staticmethod
    def get_players():
        options = ['easy', 'user', 'medium', 'hard']
        while True:
            players = input("Input command: ").split()
            if len(players) < 3 and players[0] != 'exit':
                print("Bad parameters!")
            elif len(players) == 1 and players[0] == 'exit':
                return ['exit']
            elif players[1] not in options or players[2] not in options:
                print("Bad parameters!")
            else:
                return players[1:]


if __name__ == '__main__':
    t = TicTacToe()
    while True:
        players = t.get_players()
        if players[0] == 'exit':
            break
        t.init_game()
        t.print_game()
        game_on = True
        while game_on:
            for p in players:
                if p == 'user':
                    t.human_move()
                elif p == 'easy':
                    t.make_easy_move()
                elif p == 'medium':
                    t.make_medium_move()
                else:
                    t.make_hard_move()
                result = t.count_winner()
                if result:
                    print(result)
                    game_on = False
                    break

