"""Pacman"""

from pacman_board import Board
from getch import _Getch
import os
import random
import sys

class Bcolors(object):
    """Colors"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Bunch(object):
    """Mutable named tuple.

    Usage:  point = Bunch(datum=y, squared=y*y, coord=x)
            if point.squared > threshold:
                point.isok = 1
    """
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

class Person(object):
    """docstring"""
    def __init__(self, board, position):
        self.position = position
        if board.board[position.y][position.x] == 'C':
            board.coins -= 1
        if self.__class__ is Pacman:
            board.board[position.y][position.x] = 'P'
        elif self.__class__ is Ghost:
            board.board[position.y][position.x] = 'G'
        else:
            return

    def move(self, turn):
        """Move"""
        pass

    def update_position(self, board, position):
        """Update position"""
        if self.__class__ is Pacman:
            board.board[position.y][position.x] = 'P'
        elif self.__class__ is Ghost:
            board.board[position.y][position.x] = 'G'

class Pacman(Person):
    """Pacman class"""
    def __init__(self, board, position):
        Person.__init__(self, board, position)
        self.score = 0
        self.alive = True

    def update_position(self, board, turn):
        if turn == 'w':
            new_position = Bunch(y=self.position.y - 1, x=self.position.x)
        elif turn == 'a':
            new_position = Bunch(x=self.position.x - 1, y=self.position.y)
        elif turn == 's':
            new_position = Bunch(y=self.position.y + 1, x=self.position.x)
        elif turn == 'd':
            new_position = Bunch(x=self.position.x + 1, y=self.position.y)
        else:
            return -1
        if board.board[new_position.y][new_position.x] in ['.', 'C']:
            if board.board[new_position.y][new_position.x] == 'C':
                self.collect_coin(board)
            board.board[self.position.y][self.position.x] = '.'
            board.board[new_position.y][new_position.x] = 'P'
            self.position = new_position

    def collect_coin(self, board):
        self.score += 1
        board.coins -= 1

    def check_alive(self, ghost):
        if self.position.y == ghost.position.y and self.position.x == ghost.position.x:
            self.alive = False
            return False
        else:
            return True

    def pacman_position(self):
        return self.position.x, self.position.y

class Ghost(Person):
    """Ghost class"""
    def __init__(self, board, position):
        Person.__init__(self, board, position)
        self.position_object = '.'

    def update_position(self, board):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        new_position = Bunch(x=self.position.x+x, y=self.position.y+y)
        if board.board[new_position.y][new_position.x] in ['.', 'C', 'P']:
            new_position_object = board.board[new_position.y][new_position.x]
            board.board[self.position.y][self.position.x] = self.position_object
            board.board[new_position.y][new_position.x] = 'G'
            self.position_object = new_position_object
            self.position = new_position
        # elif board.board[new_position.y][new_position.x] == 'P':
        #     board.board[new_position.y][new_position.x] = 'G'
        #     self.position = new_position
        #     print self.position.x,self.position.y

    def check_ghost(self, position):
        if self.position == position:
            return True
        else:
            return False

    def ghost_position(self):
        return self.position.x, self.position.y

def main(score=0, next_level=0):
    os.system("clear")
    getch = _Getch()
    board = Board(coins=10)
    position = Bunch(x=12, y=12)
    pacman = Pacman(board, position)
    if next_level > 0 and score > 0:
        print "Next level\n"
        pacman.score = score
    score = 0
    next_level = 0
    position = Bunch(x=4, y=5)
    ghost1 = Ghost(board, position)
    position = Bunch(x=12, y=5)
    ghost2 = Ghost(board, position)
    position = Bunch(x=22, y=5)
    ghost3 = Ghost(board, position)
    board.print_board()
    print "Score: %d" % pacman.score
    print "Enter input: "
    turn = getch()
    while turn != 'q':
        pacman.update_position(board, turn)
        ghost1.update_position(board)
        ghost2.update_position(board)
        ghost3.update_position(board)
        os.system("clear")
        board.print_board()
        if (not pacman.check_alive(ghost1) or not pacman.check_alive(ghost2) or 
                not pacman.check_alive(ghost3)):
            print "\n\t\tGame over!!!", "Your score %d\n\n" % pacman.score
            turn = 'q'
            sys.exit(0)
        elif not board.coins:
            print "\n\t\tYou won!!!", "Your score %d\n\n" % pacman.score
            main(pacman.score, next_level=1)
            turn = 'q'
        else:
            print "Score: %d" % pacman.score
            print "Enter input: "
            # turn = raw_input()
            turn = getch()


if __name__ == '__main__':
    main()
