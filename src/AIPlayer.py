from Player import Player

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

    """
    """
    def decision_function(self):
        options = self.board
        index = options[(random() * 10) % len(options)] # get valid index in options
        return self.board.drop_piece(self.colour, index)


class AIHard(AIPlayer):
     """
    """
    def decision_function(self):
        options = self.board._n
        

    
    




