"""
=== Module Description ===
This module contains the class that creates and edits the attach 4 board.
"""
from typing import List

# CONSTANTS
RED = 'R'
BLUE = 'B'
EMPTY = ''


class Attach4Board:
    """
    An nxm rectangular grid, which includes red, blue or empty cells.
    """
    # Private Attributes:
    # _n
    #   the height of the grid
    # _m
    #   the width of the grid
    # _grid
    #   the grid representation of the board
    _n: int
    _m: int
    _grid: List[List]

    def __init__(self, n, m):
        """
        Attach4Board with a grid of dimensions nxm and all cells
        initialized as EMPTY

        Note:
            Grid symbols are represented as letters defined by RED or BLUE
            The empty space is represented as EMPTY

        """
        self._n = n
        self._m = m
        self._grid = []
        for height in range(self._n):
            self._grid.append([])
            for width in range(self._m):
                self._grid[height].append(EMPTY)

