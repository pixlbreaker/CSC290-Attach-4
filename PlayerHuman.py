"""
=== Module Description ===
This module contains a class for a human player.
"""

import Player
import board


class PlayerHuman():
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
    _game_board: board

    def __init__(self, game_board: board, colour: str):
        """
        Creates a new human player with the specified disc colour
        and game board.
        """
        self.colour = colour
        self._game_board = game_board

    def move(self, column: int) -> None:
        """
        Drops a disc with this players colour at the specified
        column.
        """
        self._game_board.drop_piece(self.colour, column)

    def get_colour(self) -> str:
        """
        Returns the colour of this player's discs.
        """
        return self.colour
