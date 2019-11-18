from scr.board import *
from src.button import *
import pygame
from pygame import Rect
import math

Blue = (26, 83, 255)
White = (255, 255, 255)
DarkBlue = (0, 38, 153)
Red = (255, 40, 40)
Yellow = (255, 255, 51)
SQ = 100

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

    def __init__(self, width=820, height=800, board = Board(7,8)) -> None:
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
        self.icon = pygame.image.load('assets/4.png')
        self.game_title = pygame.image.load('assets/game_title.png')
        pygame.display.set_icon(self.icon)
        

        # Select the board image, as well as the two player images
        #self.p1 = pygame.image.load('assets/redcircle.png')
        #self.p2 = pygame.image.load('assets/yellowcircle.png')
        #self.board = pygame.image.load('assets/board.png')
        self.board = board
        

        # Add buttons to the game
        self.buttons = []
        self.menu = self.display_main_menu
        #self.start_game()
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
       
        #self.screen.fill((184, 205, 255))
        #self.screen.blit(self.p1, (208, 0))
        #self.screen.blit(self.p2, (408, 0))
        #self.screen.blit(self.board, (-1, 128))
        
        width = self.board.get_col() * SQ
        height = self.board.get_row()+1 * SQ
        size = (width, height)
        pygame.draw.rect(self.screen, White, (0, 100, 820, 800))
        pygame.draw.rect(self.screen, DarkBlue, (0, 98, 820, 800))
        for c in range(self.board.get_col()):
            for r in range(self.board.get_row()):
                pygame.draw.rect(self.screen, Blue, (c*SQ+10, r*SQ+SQ+10, SQ,SQ))
                if self.board.get_grid()[r][c] == " ":
                    
                    pygame.draw.circle(self.screen, DarkBlue, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3+3))

                    pygame.draw.circle(self.screen, White, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3))
                elif self.board.get_grid()[r][c] == "R":
                    pygame.draw.circle(self.screen, DarkBlue, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3+3))
                    pygame.draw.circle(self.screen, Red, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3))
                else:
                    pygame.draw.circle(self.screen, DarkBlue, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3+3))
                    pygame.draw.circle(self.screen, Yellow, (int(c*SQ+SQ/2+10),
                                                        int(r*SQ+SQ+SQ/2+10)), int(SQ/3))
        pygame.display.update()

        
    def display_main_menu(self) -> None:
        """
        Creates the main menu page, with included buttons
        """
        self.screen.fill((184, 205, 255))
        self.screen.blit(self.game_title, (120, self.height//8))

        start_game_button = Button(Rect(self.width / 2 - 75,
                                        self.height / 2 - 10, 150, 25),
                                   self.start_game, (255, 255, 255),
                                   'Start Game')

        end_game_button = Button(Rect(self.width / 2 - 75,
                                      self.height / 2 + 20, 150, 25),
                                 self.end_game, (255, 255, 255),
                                 'Quit Game')

        self.buttons.append(start_game_button)
        self.buttons.append(end_game_button)

    def end_game(self) -> None:
        """
        Ends the game process
        """
        self.loop = False

    def game_loop(self) -> None:
        """
        Runs the game process until the user decides to exit the game
        """

        while self.loop:
            for event in pygame.event.get():
                # Closes the game if the user closes the window.
                if event.type == pygame.QUIT:
                    self.loop = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQ))

                    if self.board.get_whos_turn() == "R":
                        self.board.drop_piece("R", col)
                    else:
                        self.board.drop_piece("Y", col)
                        
                if len(self.buttons) == 0:
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(self.screen, White, (0,0,self.width, SQ-2))
                        posx = event.pos[0]
                        if self.board.get_whos_turn() == "R":
                            pygame.draw.circle(self.screen, Red, (posx, int(SQ/2)), int(SQ/2-5))
                        else:
                            pygame.draw.circle(self.screen, Yellow, (posx, int(SQ/2)), int(SQ/2-5))
                        
                pygame.display.update()

                # Check if a button can react to the event
                for button in self.buttons:
                    button.update(event)

            self.menu()
            for button in self.buttons:
                button.display(self.screen)
            #self.make_game()
            pygame.display.update()

        # Terminate
        pygame.quit()
