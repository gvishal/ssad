import unittest
from pacman_game import *

class Tests(unittest.TestCase):

    def test_1(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        x, y = pacman.pacman_position()
        self.failUnless(x == 12 and y == 12)

    def test_2(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        x, y = ghost1.ghost_position()
        self.failUnless(x == 4 and y == 5)

    def test_3(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 'w'
        pacman.update_position(board, turn)
        x, y = pacman.pacman_position()
        self.failUnless(x == 12 and y == 11)

    def test_4(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 'a'
        pacman.update_position(board, turn)
        x, y = pacman.pacman_position()
        self.failUnless(x == 11 and y == 12)

    def test_5(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 's'
        pacman.update_position(board, turn)
        x, y = pacman.pacman_position()
        self.failUnless(x == 12 and y == 12)

    def test_6(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 'd'
        pacman.update_position(board, turn)
        x, y = pacman.pacman_position()
        self.failUnless(x == 13 and y == 12)

    def test_7(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        self.failUnless(int(board.coins) == 10)

    def test_8(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 'd'
        pacman.update_position(board, turn)
        self.failUnless((pacman.score==0 and board.coins == 10) or (pacman.score==1 and board.coins == 9))

    def test_9(self):
        board = Board(coins=10)
        position = Bunch(x=12, y=12)
        pacman = Pacman(board, position)
        position = Bunch(x=4, y=5)
        ghost1 = Ghost(board, position)
        turn = 'q'
        x = pacman.update_position(board, turn)
        self.failUnless(x == -1)
