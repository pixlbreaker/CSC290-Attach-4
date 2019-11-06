"""
=== Module Description ===
This module contains an abstract class for a player.
"""
from typing import Union, Tuple
import board


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
    _game_board: board

    def move(self) -> Union[Tuple, None]:
        """
        Returns the coordinates of where this player puts a disc
        as a Tuple or None if the player cannot make a move.
        """
        pass
