"""
=== Module description ===
This module's job is to represent the
button with its certain function
"""
from src.board import *
from typing import Tuple
import pygame
from pygame import Rect


class Button:
    """A class that creates the buttons for the gui

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

    def __init__(self, rect: Rect, on_click,
                 colour: Tuple[int, int, int] = None, text: str = ''):
        """
        Creates a button with attributes

        Note:
            If colour is none then the button is invisible

            on_click is a function that will exectute when the
            button has been pressed
        """
        self.rect = rect
        self.colour = colour
        self.text = text
        self.on_click = on_click
        self.font = pygame.font.SysFont('Arial', 36,
                                        bold=True, italic=False)
        self.set_text(text)
        self.is_hovered = False

    def set_text(self, text: str) -> None:
        """
        Sets the text on the button
        """
        self.text_image = self.font.render(text, True, (0, 0, 0))

    def display(self, screen: pygame.Surface) -> None:
        """
        Displays the button with the text centered
        """
        if self.colour is not None:
            screen.fill(self.colour, self.rect)

            rect = self.text_image.get_rect()
            rect.center = self.rect.center
            screen.blit(self.text_image, rect)

            if self.is_hovered:
                screen.fill((180, 180, 180), self.rect,
                            pygame.BLEND_RGB_MULT)

    def update(self, event) -> None:
        """
        Executes the function (on_click) when the button is pressed
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_click()

        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_hovered = True
            else:
                self.is_hovered = False
