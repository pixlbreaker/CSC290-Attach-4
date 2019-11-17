from Player import Player
from random import random
from typing import List, Tuple
import operator

# Inherits from the abstract Player class
class AIPlayer(Player):

    """
    AI player abstract class. This class should not be
    instantiated and should instead be used by subclasses
    of different single player difficulty modes.

    === Public Attributes ===
    colour:
        The colour of this player's discs.
    """

    def __init__(self, colour, board):
        self.colour = colour
        self.board = board
        
    def move(self):
        super.move()

    def get_colour(self):
        super.get_colour()

    def get_board(self):
        return self.board

    def decision_function(self):
        return


class AIEasy(AIPlayer):

    """The class AIEasy implements the easy diificulty level
    mode and makes moves based on random number generation. 
    """
    def decision_function(self):
        options = self.board.move_option()
        if options == [] : return None
        index = options[(random() * 10) % len(options)] # get valid index in options
        return self.board.drop_piece(self.colour, index)


class AIHard(AIPlayer):
    """The class AIHard implements the hard diificulty level
    mode. The class is based off of an adaptation of the 
    optimal solution to Connect 4.
    """
    def decision_function(self):
        """Computes the index to drop the next disc in. More specifically
        the function calculates a list of all potential next moves and 
        calculates the path score in each direction (check get_path_scores).
        Then returns the highest scoring index in the list of potential 
        moves. This is not the optimal solution.
        """
        if self.board.is_board_full() : return None
        indices = self.board.move_options()
        scores = {}
        for i in range(0, len(indices)):
            scores.setdefault(indices[i], self.get_path_scores(indices[i]))
        if len(scores) < 1 : return None
        return max(scores.items(), key=operator.itemgetter(1))[0]


    def get_path_scores(self, index: Tuple[int, int]):
        """ Computes the lengths of every path (a path is defined as a diagonal,
        horizontal or vertical arrangement of consecutive discs of the same
        colour) of a given index in the board attribute.

        """
        path_scores = 0
        for x_delta in range(-1, 2):
            for y_delta in range(-1, 2):
                path_scores += self.get_path_length(index, x_delta, y_delta)
        return path_scores

    def get_path_length(self, index: Tuple[int, int], x_delta, y_delta) -> 0:
        """ Traverses a path in direction of x_delta and y_delta . 
        ======== Parameters ==========

        x_delta : int
            the amount to change by with every iteration in the column direction
            e.g -1 for any path in the left direction
        y_delta : int
            the amount to change by with every iteration in the row direction
            e.g -1 for any path in the downwards direction of the board
        """
        row, column, score, i = index[0], index[1], 0, 0
        ref_colour = self.colour
        if ref_colour == ' ' : return score
        while (0 < row + y_delta < self.board._n) and \
            (0 < column + x_delta < self.board._m):
            row += y_delta
            column += x_delta
            if (self.board[row][column] == ref_colour):
                score += 1 
            elif (i == 0):
                score += 1
                ref_colour = self.board[row][column]
            else : break
            i += 1

        return score 

                





