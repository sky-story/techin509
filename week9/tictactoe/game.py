import numpy
import random


class Board:
    def __init__(self):
        # 3x3 empty board initialized
        self._board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self._board:
            print("|".join(row))
            print("-" * 5)

    def is_full(self):
        return all(cell != ' ' for row in self._board for cell in row)

    def make_move(self, x, y, player):
        if self._board[x][y] == ' ':
            self._board[x][y] = player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            # rows
            if self._board[i][0] == self._board[i][1] == self._board[i][2] != ' ':
                return self._board[i][0]
            # columns
            if self._board[0][i] == self._board[1][i] == self._board[2][i] != ' ':
                return self._board[0][i]
        # diagonals
        if self._board[0][0] == self._board[1][1] == self._board[2][2] != ' ':
            return self._board[0][0]
        if self._board[0][2] == self._board[1][1] == self._board[2][0] != ' ':
            return self._board[0][2]
        return None

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self._board[x][y] == ' '

class Game:
    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = 'X'

    def run(self):
        print("Tic Tac Toe Game Started!\n")
        print("Player 'X' goes first")
        while True:
            self._board.display()
            if self._current_player == 'X':
                x, y = self._playerX.get_move(self._board)
            else:
                x, y = self._playerO.get_move(self._board)

            self._board.make_move(x, y, self._current_player)
            winner = self._board.check_winner()
            if winner:
                self._board.display()
                print(f"Player {winner} wins!")
                break
            if self._board.is_full():
                self._board.display()
                print("It's a draw!")
                break

            # Switch player
            self._current_player = 'O' if self._current_player == 'X' else 'X'

class Human:
    def get_move(self, board):
        while True:
            try:
                move = input(f"Please enter your move as x,y coordinates. i.e. 0,2(0-indexed): ")
                x, y = map(int, move.split(','))
                if board.is_valid_move(x, y):
                    return x, y
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input format. Please enter row,col as integers.")

class Bot:
    def get_move(self, board):
        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if board.is_valid_move(x, y):
                print(f"Bot chooses: {x}, {y}")
                return x, y

# Start the game
if __name__ == "__main__":
    game = Game(Human(), Bot())
    game.run()
