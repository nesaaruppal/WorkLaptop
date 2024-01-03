'''Sudoku Solver and Generator implemented in Python'''

__author__ = 'Random Coder 59'
__version__ = '1.0.1'
__email__ = 'randomcoder59@gmail.com'

from random import shuffle
import time

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

class Sudoku:
    '''Sudoku class for solving and generating boards'''

    @classmethod
    def str_board(cls, board):
        '''Returns a board in string format'''

        str_board = ''
        for y in range(len(board)):
            if y in [3, 6]:
                str_board += '- ' * 11 + '\n'
            for x in range(len(board[y])):
                if x in [3, 6]:
                    str_board += '| '
                if x == 8:
                    str_board += str(board[y][x]) + '\n'
                else:
                    str_board += str(board[y][x]) + ' '
        return str_board

    @classmethod
    def find_empty(cls, board):
        '''Find and returns a empty cell if any, else returns None'''

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    return y, x
        return None

    @classmethod
    def valid(cls, board, num, pos):
        '''Returns if a number is valid on a position on the board'''

        for x in range(len(board[0])):
            if board[pos[0]][x] == num and pos[1] != x:
                return False

        for y in range(len(board)):
            if board[y][pos[1]] == num and pos[0] != y:
                return False

        box_y = (pos[0] // 3) * 3
        box_x = (pos[1] // 3) * 3

        for y in range(box_y, box_y + 3):
            for x in range(box_x, box_x + 3):
                if board[y][x] == num and (y, x) != pos:
                    return False

        return True

    @classmethod
    def solve(cls, board):
        '''Solves a given board and returns the board. Returns False is the board is not solvable'''
        find_result = cls.find_empty(board)
        if not find_result:
            return board
        else:
            y, x = find_result

        for num in range(1, 10):
            if Sudoku.valid(board, num, (y, x)):
                board[y][x] = num
                if Sudoku.solve(board):
                    return board
                board[y][x] = 0
        return False

    @classmethod
    def create_empty(cls, board, number):
        '''Creates empty spaces in board according to number, returns the board'''
        coors = [(y, x) for y in range(9) for x in range(9)]
        shuffle(coors)
        for idx in range(number):
            y, x = coors[idx]
            board[y][x] = 0
        return board

    @classmethod
    def generate_board(cls):
        '''Generates a random Sudoku board and returns it.'''
        numbers = list(range(1, 10))
        board = [[0 for _ in range(9)] for _ in range(9)]
        for y in range(len(board)):
            for x in range(len(board[0])):
                shuffle(numbers)
                for num in numbers:
                    if Sudoku.valid(board, num, (y, x)):
                        board[y][x] = num

                    if Sudoku.solve(board):
                        break

                    board[y][x] = num
        return board

solver = Sudoku()
print('Original board')
print(solver.str_board(board))

t1 = time.time()
solver.solve(board)
t2 = time.time()
print('Solved puzzle')
print(solver.str_board(board))
print(f'Finished in {round(t2 - t1, 3)} seconds')