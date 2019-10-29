"""
=== Module description ===
This module's job is to test the functionality's logic (testing
the if the difficulty levels are effective) and that it does not
break (testing various error conditions).
"""
# Import classes from project files
# uncomment later
# from board.py import *
# from main.py import *
import unittest



# Skeleton of test suite w/o implementation
class Tester(unittest.TestCase):
    """ All test cases testing the logic and completeness of the Attach 4 game.
    """

    def set_up_game_env(self):  # -> Game: once implemented
        """ Call init() in main and set-up the required environment
        for test cases to run in."""
        # Only makes sense to implement after the game loop is complete

        # TODO
        return None

    # need to prefix test functions with "test" so that they run during when invoking unitest
    def test_easy_vs_hard(self):
        """ Simulate a game played between the Easy AI difficulty and
        the hard AI difficulty level and test whether hard wins."""
        # self.set_up_game_env()

        # TODO
        return None

    def test_bad_user_input(self):
        """ Simulate a game played between the Easy AI difficulty and
        the hard AI difficulty level and test whether hard wins."""
        # self.set_up_game_env()


        # TODO
        return None

    # add more test cases during the development of the program as needed below ...

    def test_random_alternation(self):
        """- Added by Tomasz (Change if you want)
        Random alternation test of board.py, will end once a colour has won
        """
        from board import Board, RED, YELLOW, EMPTY
        import random
        random.seed(0)  # If you change the seed, change the return comparison
        board = Board(6, 7)
        red = True
        while (not board.is_board_full() and board.is_connected() == EMPTY):
            drop = board.drop_piece(RED if red else YELLOW, random.randint(0, 6))
            if (drop):
                red = not red
        return board.get_board() == [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                     [' ', ' ', ' ', 'R', ' ', ' ', 'R'],
                                     [' ', ' ', 'R', 'R', ' ', ' ', 'R'],
                                     [' ', 'Y', 'Y', 'Y', 'R', ' ', 'Y'],
                                     ['Y', 'Y', 'Y', 'Y', 'R', ' ', 'R'],
                                     ['R', 'Y', 'Y', 'Y', 'R', ' ', 'R']]


if __name__ == "__main__":
    unittest.main()
