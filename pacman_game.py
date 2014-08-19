"""Pacman"""

from pacman_board import Board
from getch import _Getch
import os

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

    # def update_position(self, board, position):
    #     if self.__class__ is Pacman:
    #         board.board[position.y][position.x] = 'P'
    #     elif self.__class__ is Ghost:
    #         board.board[position.y][position.x] = 'G'

class Pacman(Person):
    """Pacman class"""
    def __init__(self, board, position):
        Person.__init__(self, board, position)
        self.score = 0

    def update_position(self, board, turn):
        new_position = Bunch()
        if turn == 'w':
            new_position = Bunch(y=self.position.y - 1, x=self.position.x)
        elif turn == 'a':
            new_position = Bunch(x=self.position.x - 1, y=self.position.y)
        elif turn == 's':
            new_position = Bunch(y=self.position.y + 1, x=self.position.x)
        elif turn == 'd':
            new_position = Bunch(x=self.position.x + 1, y=self.position.y)
        if board.board[new_position.y][new_position.x] in ['.', 'C']:
            if board.board[new_position.y][new_position.x] == 'C':
                self.collect_coin(board)
            board.board[self.position.y][self.position.x] = '.'
            board.board[new_position.y][new_position.x] = 'P'
            self.position = new_position
        # elif board.board[new_position.y][new_position.x] == 'C':
        #     board.board[self.position.y][self.position.x] = '.'
        #     board.board[new_position.y][new_position.x] = 'P'
        #     self.position = new_position

    def collect_coin(self, board):
        self.score += 1
        board.coins -= 1

class Ghost(Person):
    pass

def check_ghost():
    pass

def ghost_position():
    pass

def check_wall():
    pass

def main():
    os.system("clear")
    getch = _Getch()
    board = Board(coins=2)
    position = Bunch(x=12, y=12)
    pacman = Pacman(board, position)
    position = Bunch(x=4, y=4)
    ghost = Ghost(board, position)
    board.print_board()
    print "Score: %d" % pacman.score
    print "Enter input: "
    turn = getch()
    print turn
    while turn != 'q':
        pacman.update_position(board, turn)
        os.system("clear")
        board.print_board()
        if not board.coins:
            print "\n\t\tYou won!!!","Your score %d\n\n" % pacman.score
            turn = 'q'
        else:
            print "Score: %d" % pacman.score
            print "Enter input: "
            # turn = raw_input()
            turn = getch()


if __name__ == '__main__':
    main()
