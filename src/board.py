"""
=== Module Description ===
This module contains the class that creates and edits the attach-4 board.
"""
from typing import List

# CONSTANTS
RED = 'R'
YELLOW = 'Y'
EMPTY = ' '


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

    def __init__(self, height: int, width: int):
        """
        Board with a grid of dimensions nxm and all cells
        initialized as EMPTY

        Note:
            Grid symbols are represented as letters defined by RED or BLUE
            The empty space is represented as EMPTY
        """
        self._turn = 0
        self._n = height
        self._m = width
        self._grid = []
        for height in range(self._n):
            self._grid.append([])
            for width in range(self._m):
                self._grid[height].append(EMPTY)

    def drop_piece(self, colour: str, column: int) -> bool:
        """
        Returns true if the piece is dropped in the given column.
        Returns false if the piece cannot be dropped.

        Note:
            If the column is not full the piece must drop to the top
            most available row in the given column.
            If the entire column is already full the drop cannot occur.
        """
        result = self.get_drop_y(column)
        if result == -1:
            return False

        self._grid[result][column] = colour  # The piece is placed
        self._turn += 1
        return True

    def get_drop_y(self, column):
        for row in range(self._n-1, -1, -1):
            if self._grid[row][column] == EMPTY:
                return row

        return -1

    def is_connected(self) -> str:
        """
        Returns the colour of the tile that contains a diagonal, vertical or a
        horizontal linear combination with 4 or more pieces of the same color.

        Note:
            If there is no connection then EMPTY is returned.
        """
        for column in range(self._m):
            for row in range(self._n):
                piece_colour = self._grid[row][column]
                if piece_colour != EMPTY:  # Is a coloured tile
                    if self._check_connected(piece_colour, column, row, -1, 1):
                        return piece_colour
                    if self._check_connected(piece_colour, column, row, 0, 1):
                        return piece_colour
                    if self._check_connected(piece_colour, column, row, 1, 1):
                        return piece_colour
                    if self._check_connected(piece_colour, column, row, 1, 0):
                        return piece_colour

        return EMPTY  # There is no connection

    def _check_connected(self, colour: str, column: int,
                         row: int, dx: int, dy: int) -> bool:
        """
        This is a private method that returns true iff a tile with given colour
        has a connection in dx, dy of 4 pieces
        """
        count = 0
        while self.is_valid_cell(row, column):

            if count >= 4:
                return True
            elif self._grid[row][column] != colour:
                return False
            # Increment
            count += 1
            row += dy
            column += dx

        return count >= 4  # There is no connection

    def is_board_full(self) -> bool:
        """
        Returns true iff there are no EMPTY cells in the grid
        """

        for column in range(self._m):
            if self._grid[0][column] == EMPTY:  # Check if the top row is EMPTY
                return False

        return True

    def is_valid_cell(self, row: int, column: int):
        """
        Return true iff the (row,column) are in the bounds of the nxm dimension
        """
        if 0 <= row < self._n and 0 <= column < self._m:
            return True
        return False

    def get_piece(self, row: int, column: int) -> str:
        """
        Returns the piece that the grid contains at the given row, column
        """
        return self._grid[row][column]

    def get_board(self) -> List[List]:
        """
        Returns the grid representation of the board
        """
        return self._grid

    def __str__(self) -> str:
        """
        Returns the string representation of the board
        """
        final = ""
        for line in self.get_board():
            final += "|"
            final += "|".join(line)
            final += "|\n"
        return final

    def move_options(self) -> List[tuple]:
        """ Search self._n columns and record
        the co-ordinates that have enough room
        to drop a piece into.
        """
        if self.is_board_full():
            return []

        options = []
        for col in range(0, self._m):
            for row in range(self._n-1, -1, -1):
                if self._grid[row][col] == EMPTY:
                    options.append(tuple([row, col]))
                    break

        return options

    def is_option(self, index) -> bool:
        """
        Returns true iff the drop is possible
        """
        row, col = index[0], index[1]
        if self._grid[row][col] != EMPTY:
            return False

        if row+1 < self._n and self._grid[row+1][col] == EMPTY:
            return False
        return True

    def get_col(self) -> int:
        """
        Returns the number of columns in the game
        """
        return self._m

    def get_row(self) -> int:
        """
        Returns the number of row in the game
        """
        return self._n

    def get_grid(self) -> list:
        """
        Returns the current grid of the game
        """
        return self._grid

    def get_whos_turn(self):
        """
        Returns the current move of the players colour
        """
        if self._turn % 2 == 0:
            return "R"
        else:
            return "Y"
