from board import *
import pygame
import os

#TODO: Initialize a Main Menu

#Access to path
path_name = os.path.dirname("CSC290-Attach-4")

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

    def __init__(self, width = 720, height = 740) -> None:
        """
        Initialize a screen with dimensions (width, height),
        then 
        """
        pygame.init()
        
        #Set screen dimensions with given <width> and <height>
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((255,255,255))
        
        #Set the Title and Icon
        pygame.display.set_caption("Attach 4")
        icon = os.path.join(path_name, 'Icon set','4.png')
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)
        
        #Select the board image, as well as the two player images
        p1 = os.path.join(path_name, 'Icon set','redcircle.png')
        p2 = os.path.join(path_name, 'Icon set','yellowcircle.png')
        board = os.path.join(path_name, 'Icon set','board.png')
        self.p1 = pygame.image.load(p1)
        self.p2 = pygame.image.load(p2)
        self.board = pygame.image.load(board)

        #Create game
        self.make_game()

    def make_game(self) -> None:
        """
        Creates the Attach 4 board and shows both player pieces.
        Game ends once a player has won, or a tie has been reached.
        """
        self.screen.blit(self.p1, (208,0))
        self.screen.blit(self.p2, (408, 0))
        self.screen.blit(self.board, (-1, 128))
        pygame.display.update()
    

    def quit(self) -> None:
        """
        Closes the game if the user closes the window.
        """
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
            elif events.type == KEYDOWN:
                break
    
