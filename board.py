"""
=== Module Description ===
This module contains the class that creates and edits the attach-4 board.
"""
from typing import List

# CONSTANTS
RED = 'R'
YELLOW = 'Y'
EMPTY = ''


class Board:
    """
    An nxm rectangular grid, which includes red, yellow or empty cells.
    """
    # Private Attributes:
    # _n
    #   the height of the grid
    # _m
    #   the width of the grid
    # _grid
    #   the grid representation of the board
    #   Example of an empty 3x3 grid:
    #   [ ['', '', '' ],
    #     ['', '', '' ],
    #     ['', '', '' ] ]

    _n: int
    _m: int
    _grid: List[List]

    def __init__(self, n: int, m: int):
        """
        Board with a grid of dimensions nxm and all cells
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

    def drop_piece(self, col: int) -> bool:
        """
        Returns true if the piece can be dropped in the given column.

        Note:
            If the column is not full the piece must drop to the top
            most available row in the given column.
            If the entire column is already full the drop cannot occur.
        """
        pass

    def is_connected(self) -> bool:
        """
        Returns true iff the board contains a diagonal, vertical or a horizontal
        linear combination with 4 or more pieces of the same color.
        """
        pass

    def is_board_full(self) -> bool:
        """
        Returns true iff there are no EMPTY cells in the grid

        Precondition:
            There are no EMPTY cells underneath a piece
        """
        for col in range(self._m):
            if self._grid[0][col] == EMPTY: # Only check if the top row is EMPTY
                return False
        return True

    def get_piece(self, row: int, col: int) -> str:
        """
        Returns the piece that the grid contains at the given row, column
        """
        return self._grid[row][col]

    def get_board(self) -> List[List]:
        """
        Returns the grid representation of the board
        """
        return self._grid

