"""
=== Module Description ===
This module contains a class for a human player.
"""
from src.Player import Player
from src.board import Board


class PlayerHuman(Player):
    """
        A human player which makes moves by clicking
        on the column that they want to drop their disc.

        === Public Attributes ===
        colour:
            The colour of this player's discs.
        """
    # Private Attributes:
    # _game_board
    #   the board that this player is playing on.
    colour: str
    _game_board: Board

    def __init__(self, colour: str, game_board: Board):
        """
        Creates a new human player with the specified disc colour
        and game board.
        """
        self.colour = colour
        self._game_board = game_board

    def move(self, column: int) -> bool:
        """
        Drops a disc with this players colour at the specified
        column then returns whether the move was successful.
        """
        return self._game_board.drop_piece(self.colour, column)
