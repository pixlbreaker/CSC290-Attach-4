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
        return self.colour

    def get_board(self):
        return self.board

    def decision_function(self):
        return


class AIEasy(AIPlayer):

    """The class AIEasy implements the easy diificulty level
    mode and makes moves based on random number generation. 
    """
    def decision_function(self):
        options = self.board.move_options()
        if options == [] : return None
        index = options[int(random() * 10) % len(options)] # get valid index in options
        return index

    def get_colour(self):
        self.get_colour()


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
            scores.setdefault(indices[i], self.all_path_scores(indices[i]))
        if len(scores) < 1 : return None
        print("Scores: " +str(scores))
        return self.interpret_scores(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))


    def all_path_scores(self, index: Tuple[int, int]):
        """ Computes the lengths of every path (a path is defined as a diagonal,
        horizontal or vertical arrangement of consecutive discs of the same
        colour) of a given index in the board attribute.

        """
        path_scores = 0
        for x_delta in range(-1, 2):
            for y_delta in range(-1, 2):
                if (x_delta == 0 and y_delta == 0) : continue
                path_scores += self.get_path_score(index, x_delta, y_delta)
        return path_scores

    def get_path_score(self, index: Tuple[int, int], x_delta, y_delta) -> 0:
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
            if (self.board._grid[row][column] == ref_colour):
                score += 1 
            elif (i == 0 and self.board._grid[row][column] != ref_colour and \
                self.board._grid[row][column] != ' '):
                score += 1
                ref_colour = self.board._grid[row][column]
            elif (i > 1 and self.board._grid[row][column] == ' ' and \
                self.board.is_option((row, column))):
                score += 1
                break
            else : break
            i += 1

            if (score == 3) and ref_colour == self.colour:
                score *= 3
                break
            elif (score == 3):
                score *= 2
                break
        return score 

    def interpret_scores(self, sorted_scores):
        highest, tied = sorted_scores[0][1], 0
        print("sorted: "+str(sorted_scores))
        for i in range(1, len(sorted_scores)):
            if (highest != sorted_scores[i][1]):
               break
            tied += 1
        
        current, closest, medianx, mediany = float('inf'), None, self.board._m / 2, \
            self.board._n / 2
        if tied > 0:
            for key in sorted_scores[:tied+1]:
                dist = abs(medianx - key[0][1]) + abs(mediany - key[0][0])
                if dist < current:
                    closest = key[0]
                    current = dist
            return closest
        else : return sorted_scores[0][0]
