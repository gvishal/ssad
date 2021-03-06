"""board = [
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
"""
import random

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Board(object):
    """Board class"""
    def __init__(self, coins=25):
        self.board = [['.' for x in xrange(35)]for y in xrange(15)]
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self._coins = 0
        self.generate_wall()
        self.generate_coin(coins)

    def coins():
        doc = "The coins property."
        def fget(self):
            return self._coins
        def fset(self, value):
            self._coins = value
        def fdel(self):
            del self._coins
        return locals()
    coins = property(**coins())

    def print_board(self):
        #print Bcolors.WARNING
        # print '\n'.join([''.join(['{:3}'.format(item) for item in row])
        #                                         for row in self.board])
        for row in self.board:
            color_row = []
            for item in row:
                if item == 'C':
                    color_row.append(Bcolors.HEADER + item)
                elif item == 'P':
                    color_row.append(Bcolors.OKBLUE + item)
                elif item == 'G':
                    color_row.append(Bcolors.OKGREEN + item)
                else:
                    color_row.append(Bcolors.WARNING + item)
            print ''.join(['{:8}'.format(item) for item in color_row])
        print Bcolors.ENDC

    def generate_wall(self):
        for x in xrange(self.cols):
            self.board[0][x] = 'X' 
            self.board[1][x] = 'X'
            self.board[-2][x] = 'X'
            self.board[-1][x] = 'X'
        for y in xrange(self.rows):
            self.board[y][0] = 'X'
            self.board[y][-1] = 'X'

    def generate_coin(self, N):
        for n in xrange(N):
            x = random.randint(1, self.cols-2)
            y = random.randint(2, self.rows-3)
            if self.board[y][x] != 'X':
                self.board[y][x] = 'C'
            self.coins += 1

    def position_pacman(self, position):
        self.board[position.y][position.x] = 'P'

    def position_ghost(self, position):
        self.board[position.y][position.x] = 'G'

    def check_wall(self, position):
        if self.board[position.y][position.x] == 'W':
            return True
