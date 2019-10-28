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


if __name__ == "__main__":
    unittest.main()