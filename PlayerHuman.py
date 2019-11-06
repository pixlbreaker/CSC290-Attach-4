"""
=== Module Description ===
This module contains a class for a human player.
"""

import Player
import board


class PlayerHuman():
    """
        A player abstract class. This class should not be
        instantiated and should instead be used by subclasses.

        === Public Attributes ===
        colour:
            The colour of this player's discs.
        """
    # Private Attributes:
    # _game_board
    #   the board that this player is playing on.
    colour: str
    _game_board: board

    def __init__(self, game_board: board, colour: str):
        """

        """
        self.colour = colour
        self._game_board = game_board

    def move(self, column: int) -> None:
        """

        """
        self._game_board.drop_piece(self.colour, column)

    def get_colour(self) -> str:
        """
        Returns the colour of this player's discs.
        """
        return self.colour
