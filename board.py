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

    Representation Invariant:
            There are no EMPTY cells underneath a piece
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

    def drop_piece(self, col: int, colour: str) -> bool:
        """
        Returns true if the piece is dropped in the given column.
        Returns false if the piece cannot be dropped.

        Note:
            If the column is not full the piece must drop to the top
            most available row in the given column.
            If the entire column is already full the drop cannot occur.
        """
        if self._grid[0][col] != EMPTY:  # Check if the column is full
            return False
        for row in range(self._n-1, -1, -1):
            if self._grid[row][col] == EMPTY:
                self._grid[row][col] = colour  # The piece is placed
                return True

        return False  # If no piece can be dropped

    def is_connected(self) -> str:
        """
        Returns the colour of the tile that contains a diagonal, vertical or a
        horizontal linear combination with 4 or more pieces of the same color.
        """
        for col in range(self._m):
            for row in range(self._n):
                piece_colour = self._grid[row][col]
                if piece_colour != EMPTY:
                    if self._check_connected(piece_colour, col, row, -1, -1):
                        return piece_colour
                    if self._check_connected(piece_colour, col, row, 0, 1):
                        return piece_colour
                    if self._check_connected(piece_colour, col, row, 1, 1):
                        return piece_colour
                    if self._check_connected(piece_colour, col, row, 1, 0):
                        return piece_colour

    def _check_connected(self, colour: str, col: int,
                         row: int, dx: int, dy: int) -> bool:
        """
        This is a private method that returns true iff a tile with given colour
        has a connection in dx, dy of 4 pieces
        """
        pass

    def is_board_full(self) -> bool:
        """
        Returns true iff there are no EMPTY cells in the grid
        """
        for col in range(self._m):
            if self._grid[0][col] == EMPTY: # Only check if the top row is EMPTY
                return False
        return True

    def is_valid_cell(self, row: int, col: int):
        """
        Return true iff the (row,col) are in the bounds of the nxm dimension
        """
        if 0 <= row < self._n and 0 <= col < self._m:
            return True
        return False

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

