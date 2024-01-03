import random

class Minesweeper:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.flags = 0
        self.game_over = False
        self.generate_board()

    def generate_board(self):
        self.mines_placed = 0
        while self.mines_placed < self.mines:
            row = random.randint(0, self.size-1)
            col = random.randint(0, self.size-1)
            if self.board[row][col] == 0:
                self.board[row][col] = "*"
                self.mines_placed += 1
                # Place additional mines if needed
                if self.mines_placed < self.mines:
                    self.add_adjacent_mines(row, col)

    def add_adjacent_mines(self, row, col):
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r >= 0 and r < self.size and c >= 0 and c < self.size
                        and self.board[r][c] == 0):
                    self.board[r][c] = "*"

    def reveal_cell(self, row, col):
        if self.game_over:
            return
        if self.board[row][col] == "*":
            self.game_over = True
            print("Game Over!")
        elif self.board[row][col] == 0:
            self.reveal_adjacent_cells(row, col)
            self.print_board()

    def reveal_adjacent_cells(self, row, col):
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r >= 0 and r < self.size and c >= 0 and c < self.size
                        and self.board[r][c] != -1):
                    self.reveal_cell(r, c)

    def print_board(self):
        for row in self.board:
            print(" ".join([str(c) for c in row]))

    def flag_cell(self, row, col):
        if self.game_over:
            return
        if self.board[row][col] == "*":
            return
        self.board[row][col] = -1
        self.flags += 1
        if self.mines_in_area(row, col) == 0:
            self.reveal_adjacent_cells(row, col)

    def mines_in_area(self, row, col):
        count = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r >= 0 and r < self.size and c >= 0 and c < self.size
                        and self.board[r][c] == "*"):
                    count += 1
        return count

# Start the game
size = 10
mines = 10
game = Minesweeper(size, mines)
while not game.game_over:
    row = int(input("Enter the row (0-" + str(size-1) + "): "))
    col = int(input("Enter the column (0-" + str(size-1) + "): "))
    game.reveal_cell(row, col)
    if game.game_over:
        break
    choice = input("Do you want to flag a cell (y/n): ")
    if choice.lower() == "y":
        game.flag_cell(row, col)