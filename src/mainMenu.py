"""
=== Module description ===
This module's job is to run the appropriate 
assets (images/buttons) for menu state of the gui
"""
from src.util import *
from src.button import *
from src.gui import *
from typing import Tuple
import pygame
from pygame import Rect


class MainMenu:
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

    ======Private Attributes======

    """

    def __init__(self, gui):
        """
        Creates a button with attributes

        Note:
            If colour is none then the button is invisible

            on_click is a function that will exectute when the
            button has been pressed
        """
        self.gui = gui

        # Title
        self.title_rect = Rect(120,
                               self.gui.height // 8,
                               self.gui.width // 2,
                               self.gui.width // 2 * 244 / 925)

        self.title_rect.centerx = self.gui.width // 2

        self.game_title = pygame.image.load('assets/A45.png').convert_alpha()
        self.game_title = pygame.transform.smoothscale(
            self.game_title, self.title_rect.size)

        # Start Button
        start_rect = Rect(0, 0, 200, 50)
        start_rect.centerx = self.gui.width // 2
        start_rect.centery = self.gui.height // 2

        start_game_button = Button(start_rect,
                                   self.gui.start_game, (255, 255, 255),
                                   'Start Game')

        # Quit Button
        end_rect = Rect(0, 0, 200, 50)
        end_rect.centerx = self.gui.width // 2
        end_rect.centery = self.gui.height // 2 + 100

        end_game_button = Button(end_rect,
                                 self.gui.end_game, (255, 255, 255),
                                 'Quit Game')

        self.buttons = []
        self.buttons.append(start_game_button)
        self.buttons.append(end_game_button)

    def display(self, screen: pygame.Surface):
        """
        Displays the button with the text centered
        """
        screen.fill(BACKGROUND_COLOR)
        screen.blit(self.game_title, self.title_rect)

        for button in self.buttons:
            button.display(screen)

    def update(self, event):
        """
        Executes the function (on_click) when the button is pressed
        """
        for button in self.buttons:
            button.update(event)
