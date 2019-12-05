"""
=== Module description ===
This module's job is to run the appropriate 
assets (images/buttons) for in-game state of the gui
"""
from src.board import *
from src.gui import *
from src.util import *
from src.AIPlayer import *
from src.PlayerHuman import *
from typing import Tuple
import pygame
from pygame import Rect
from pygame import gfxdraw
import math
import enum

class Mode(enum.Enum):
    Two_Player = 1
    Easy = 2
    Hard = 3


class InGame:
    """
    A class that creates the buttons for the gui

    ======Public Attributes======
    rect:
        The button object, with width, height and position
    colour:
        The colour of the button.
    text:
        The text on the button.
    on_click:
        The function that will exectute when the
        button has been pressed .
    font:
        The font of the text on the button
        gui:
        The gui for the game
    rows:
        The rows for the game
    cols:
        The columns for the game
    current_col:
        The current column
    padding:
        Padding to be used as spacing
    square_size:
        Baseline for token size
    mode:
        The mode of the game
    board:
        The board for the game
    grid_rect:
        A grid version of the board used for visuals
    opponent:
        The opponent for the game

    ======Private Attributes======

    """

    def __init__(self, gui, mode: Mode) -> None:
        """
        Creates a button with attributes

        Note:
            If colour is none then the button is invisible

            on_click is a function that will exectute when the
            button has been pressed
        """
        self.gui = gui
        self.rows = 7
        self.cols = 6
        self.padding = 10
        self.square_size = 50
        self.current_col = -1
        self.mode = mode
        

        self.board = Board(self.rows, self.cols)

        self.grid_rect = Rect(0, 0,
                              self.cols * (self.square_size + 2*self.padding),
                              self.rows * (self.square_size + 2*self.padding))

        self.grid_rect.center = (400, 325)

        if (self.mode == Mode.Easy) : self.opponent = AIEasy('R',self.board)
        elif (self.mode == Mode.Hard) : self.opponent = AIHard('R', self.board)
        else : self.opponent = PlayerHuman("R",self.board)

    def display(self, screen: pygame.Surface) -> None:
        """
        Displays the button with the text centered
        """
        screen.fill(BACKGROUND_COLOR)

        self.draw_grid(screen)

        if self.current_col != -1:
            # Ghost
            self.draw_piece(screen, self.board.get_drop_y(self.current_col),
                            self.current_col,
                            self.get_ghost_color(self.board.get_whos_turn()))

            # Fill
            self.draw_piece(screen, -1, self.current_col,
                            self.get_piece_color(self.board.get_whos_turn()))

    def draw_grid(self, screen) -> None:
        """
        Draws the game board
        """
        pygame.draw.rect(screen, OUTLINE_COLOR, self.grid_rect.inflate(2, 2))
        pygame.draw.rect(screen, BOARD_COLOR, self.grid_rect)

        for col in range(self.cols):
            for row in range(self.rows):
                self.draw_piece(screen, row, col, self.get_piece_color(
                    self.board.get_grid()[row][col]))

    def get_piece_color(self, player: Player) -> None:
        """
        Returns piece colour of the given player
        """
        if player == "R":
            return PLAYER1_COLOR

        if player == "Y":
            return PLAYER2_COLOR

        return EMPTY_COLOR

    def get_ghost_color(self, player) -> None:
        """
        Returns the colour of the given ghost
        """
        if player == "R":
            return PLAYER1_GHOST_COLOR

        if player == "Y":
            return PLAYER2_GHOST_COLOR

        return EMPTY_COLOR

    def draw_piece(self, screen, row, col, fill_color) -> None:
        """
        Draws the coloured piece on the board
        """
        pos = (col * (self.square_size + 2 * self.padding) +
               self.square_size // 2 + self.padding + self.grid_rect.x,
               row * (self.square_size + 2 * self.padding) +
               self.square_size // 2 + self.padding + self.grid_rect.y)

        # Outline
        gfxdraw.aacircle(screen, pos[0], pos[1],
                         self.square_size // 2 + 1, OUTLINE_COLOR)

        # Fill
        gfxdraw.aacircle(screen, pos[0], pos[1],
                         self.square_size // 2, fill_color)

        gfxdraw.filled_circle(screen, pos[0], pos[1],
                              self.square_size // 2, fill_color)


    def update(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN \
                and (event.button == 1 or event.button == 3):

            if self.current_col != -1 and self.board.drop_piece(
                    self.board.get_whos_turn(), self.current_col):
                result = self.board.is_connected()
                if result != " " or self.board.is_board_full():
                    print("WINNER", result)
                    self.gui.goto_main_menu()
                if self.mode != Mode.Two_Player:
                    opp_move = self.opponent.decision_function()[1]
                    if self.current_col != -1 and self.board.drop_piece( \
                        self.board.get_whos_turn(), opp_move):
                        result = self.board.is_connected()
                        if result != " " or self.board.is_board_full():
                            print("WINNER", result)
                            self.gui.goto_main_menu()
        elif event.type == pygame.MOUSEMOTION:
            if self.grid_rect.collidepoint(event.pos):
                self.current_col = int(((event.pos[0] - self.grid_rect.x) /
                                        self.grid_rect.width) * self.cols)
            else:
                self.current_col = -1
    
