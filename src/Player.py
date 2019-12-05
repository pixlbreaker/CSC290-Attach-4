"""
=== Module Description ===
This module contains an abstract class for a player.
"""
from abc import ABC
from src.board import *


class Player:
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
    _game_board: Board

    def move(self) -> bool:
        """
        Drops a disc with this players colour at the specified
        column then returns whether the move was successful.
        """
        pass

    def get_colour(self) -> str:
        """
        Returns the colour of this player's discs.
        """
        return self.colour
