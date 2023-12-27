import random

class Connect4:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.turn = 0
        self.game_over = False

    def print_board(self):
        for row in self.board:
            print(" ".join([str(c) for c in row]))

    def valid_move(self, row, col):
        return (row >= 0 and row < self.size and col >= 0 and col < self.size
                and self.board[row][col] == 0)

    def move(self, row, col):
        if not self.valid_move(row, col):
            return False
        self.board[row][col] = self.turn
        self.turn = 1 - self.turn
        return True

    def winner(self):
        # Check for a horizontal win
        for row in range(self.size):
            if self.board[row][0] != 0 and self.board[row][0] == self.board[row][1] == self.board[row][2] == self.board[row][3]:
                return self.board[row][0]
        # Check for a vertical win
        for col in range(self.size):
            if self.board[0][col] != 0 and self.board[0][col] == self.board[1][col] == self.board[2][col] == self.board[3][col]:
                return self.board[0][col]
        # Check for a diagonal win
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3]:
            return self.board[0][0]
        if self.board[0][3] != 0 and self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0]:
            return self.board[0][3]
        # Check if the board is full and no one has won
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return 0
        # No one has won, so the game is a draw
        return "draw"

    def play_game(self):
        while not self.game_over:
            self.print_board()
            row = int(input("Enter row (0-" + str(self.size-1) + "): "))
            col = int(input("Enter column (0-" + str(self.size-1) + "): "))
            if self.move(row, col):
                winner = self.winner()
                if winner != 0:
                    self.game_over = True
                    print("The winner is", winner)
                    break

# Start the game
size = 6
game = Connect4(size)
game.play_game()