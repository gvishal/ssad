"""Pacman"""

from pacman_board import Board
from getch import _Getch
import os
import random

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
        if self.__class__ is Pacman:
            board.board[position.y][position.x] = 'P'
        elif self.__class__ is Ghost:
            board.board[position.y][position.x] = 'G'
        pass

    def move(self, turn):
        pass

    def update_position(self, board, position):
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
            return
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
        print self.position.x,self.position.y

class Ghost(Person):
    """Ghost class"""
    def __init__(self, board, position):
        Person.__init__(self, board, position)
        self.position_object = '.'

    def update_position(self, board):
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        new_position = Bunch(x=self.position.x+x, y=self.position.y+y)
        if board.board[new_position.y][new_position.x] in ['.','C','P']:
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
        return self.position.x,self.position.y

def check_wall():
    pass

def main():
    os.system("clear")
    getch = _Getch()
    board = Board(coins=10)
    position = Bunch(x=12, y=12)
    pacman = Pacman(board, position)
    position = Bunch(x=4, y=5)
    ghost = Ghost(board, position)
    board.print_board()
    print "Score: %d" % pacman.score
    print "Enter input: "
    turn = getch()
    while turn != 'q':
        pacman.update_position(board, turn)
        ghost.update_position(board)
        os.system("clear")
        board.print_board()
        if not pacman.check_alive(ghost):
            print "\n\t\tGame over!!!","Your score %d\n\n" % pacman.score
            turn = 'q'
        elif not board.coins:
            print "\n\t\tYou won!!!","Your score %d\n\n" % pacman.score
            turn = 'q'
        else:
            print "Score: %d" % pacman.score
            print "Enter input: "
            # turn = raw_input()
            turn = getch()


if __name__ == '__main__':
    main()
