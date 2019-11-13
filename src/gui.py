from src.board import *
from src.button import *

import pygame
from pygame import Rect


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

    def __init__(self, width=720, height=740) -> None:
        """
        Initialize a screen with dimensions (width, height),
        then
        """
        pygame.init()

        # Set screen dimensions with given <width> and <height>
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

        # Set the Title and Icon
        pygame.display.set_caption("Attach 4")
        self.icon = pygame.image.load('assets/4.png')
        pygame.display.set_icon(self.icon)
        self.menu = self.display_main_menu

        # Select the board image, as well as the two player images
        self.p1 = pygame.image.load('assets/redcircle.png')
        self.p2 = pygame.image.load('assets/yellowcircle.png')
        self.board = pygame.image.load('assets/board.png')

        # Add buttons to the game
        self.buttons = []

        self.game_loop()

    def start_game(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self.menu = self.make_game
        self.buttons.clear()

    def make_game(self) -> None:
        """
        Creates the Attach 4 board and shows both player pieces.
        Game ends once a player has won, or a tie has been reached.

        Note:
            This should be envoked every frame (to redraw to the screen)
        """
        self.menu = self.make_game
        self.buttons.clear()
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.p1, (208, 0))
        self.screen.blit(self.p2, (408, 0))
        self.screen.blit(self.board, (-1, 128))

    def display_main_menu(self) -> None:
        """
        Creates the main menu page, with included buttons
        """
        start_game_button = Button(Rect(self.width / 2 - 50,
                                        self.height / 2 - 10, 100, 20),
                                   self.start_game, (255, 255, 255),
                                   'Start Game')

        self.buttons.append(start_game_button)
        self.screen.fill((255, 0, 0))

    def game_loop(self) -> None:
        """
        Runs the game process until the user decides to exit the game
        """
        loop = True

        while loop:
            for event in pygame.event.get():
                # Closes the game if the user closes the window.
                if event.type == pygame.QUIT:
                    loop = False

                # Check if a button can react to the event
                for button in self.buttons:
                    button.update(event)

            self.menu()
            for button in self.buttons:
                button.display(self.screen)
            pygame.display.update()

        # Terminate
        pygame.quit()
