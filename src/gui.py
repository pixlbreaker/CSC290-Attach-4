"""
=== Module description ===
This module's job is to run the entire
gui for the attach 4 game
"""
from src.mainMenu import *
from src.inGame import *
import pygame


class Gui:
    """
    A class that creates the visual aspect of the game Attach 4.

    ======Public Attributes======
    width:
        The width of the screen.
    height:
        The height of the screen.

    ======Private Attributes======
    _screen:
        The screen of the game.
    _icon:
        The icon for the game.
    _p1:
        Player 1.
    _p2:
        Player 2
    _board:
        The Board for the game.
    """

    def __init__(self, width=800, height=600, board=Board(7, 8)) -> None:
        """
        Initialize a screen with dimensions (width, height),
        then
        """
        pygame.init()

        self.loop = True

        # Set screen dimensions with given <width> and <height>
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

        # Set the Title and Icon
        pygame.display.set_caption("Attach 4")
        self.icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self.icon)

        self.current_view = MainMenu(self)
        self.game_loop()

    def start_game(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self.current_view = InGame(self)

    def goto_main_menu(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self.current_view = MainMenu(self)

    def end_game(self) -> None:
        """Ends the game process."""
        self.loop = False

    def game_loop(self) -> None:
        """Runs the game process until the user decides to exit the game."""

        while self.loop:
            for event in pygame.event.get():
                # Closes the game if the user closes the window.
                if event.type == pygame.QUIT:
                    self.loop = False

                self.current_view.update(event)

            self.current_view.display(self.screen)
            pygame.display.flip()

        # Terminate
        pygame.quit()
