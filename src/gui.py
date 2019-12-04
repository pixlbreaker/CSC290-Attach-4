"""
=== Module description ===
This module's job is to create and run the entire
gui for the current Attach 4 game.
"""
from src.mainMenu import *
from src.inGame import *
from assets import *
import pygame


class Gui:
    """
    A class that creates a visual representation of the game Attach 4.

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
    _board:
        The Board for the game.
    _current_view:
        The screen currently being displayed
    """

    def __init__(self, width=800, height=600, board=Board(7, 8)) -> None:
        """
        Initialize a screen with dimensions (width, height), and create a board.
        """
        pygame.init()
        
        pygame.mixer.music.set_volume(0.2)
        self.loop = True

        # Set screen dimensions with given <width> and <height>
        self.width = width
        self.height = height
        self._screen = pygame.display.set_mode((width, height))

        # Set the Title and Icon
        pygame.display.set_caption("Attach 4")
        self._icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self._icon)

        self._current_view = MainMenu(self)
        #Begin audio playback
        self._INTRO_MUSIC = pygame.mixer.music.load("assets/Intro.wav")
        pygame.mixer.music.play(-1)
        self.game_loop()

    def start_game_two_player(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self._current_view = InGame(self, Mode.Two_Player)
        self._GAME_MUSIC = pygame.mixer.music.load("assets/DuringPlay.wav")
        pygame.mixer.music.play(-1)

    def start_game_easy(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self._current_view = InGame(self, Mode.Easy)
        self._GAME_MUSIC = pygame.mixer.music.load("assets/DuringPlay.wav")
        pygame.mixer.music.play(-1)

    def start_game_hard(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self._current_view = InGame(self, Mode.Hard)
        self._GAME_MUSIC = pygame.mixer.music.load("assets/DuringPlay.wav")
        pygame.mixer.music.play(-1)
        

    def goto_main_menu(self) -> None:
        """
        Updates the game state so it clears the menu and starts the game

        Note:
            This should be envoked once, in order to start the game.
        """
        self._current_view = MainMenu(self)
        self._INTRO_MUSIC = pygame.mixer.music.load("assets/Intro.wav")
        pygame.mixer.music.play(-1)

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

                self._current_view.update(event)

            self._current_view.display(self._screen)
            pygame.display.flip()

        # Terminate
        pygame.quit()
