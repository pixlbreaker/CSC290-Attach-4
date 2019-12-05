# CSC290 - Attach 4

## Content
1. Introduction
2. How to Play
3. Installation
4. Screenshots and Gameplay
5. Documentation
6. Individual Contributions
7. Additional Information

## Introduction
This is a Connect-4 inspired game built with python and pygame for our **CSC 290: Communication Skills for Computer Scientists**. Our team members include:

- Niral Patel
- Tomasz Cieslak
- Michael Carmine De Lisio
- Ravnit Singh Lotay
- Michael Skotar

## How to Play 🎮
**The objective of the game is to get 4 chips in a row.** This can be in any of the following orientation
- Vertically
- Horizontally
- Diagonally

### Game Play
Once you start up the game you are met with the main menu.

![Main Menu](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/titlepage.png "Main Menu")

This is a **turn-based game**, meaning that each player has a turn when they make their move. Each move consists of selecting a column to drop a chip in. This is done by selecting which column with the mouse and clicking to confirm the selection.

In this specific implementation we use mouse's position to determine where to drop the chip.

## Installation 🖥️
Our game relies on both python and pygame. Python is the programming language that our game was coded in, while pygame is the package we used to have a graphical user interface.

First we will install the game files from the releases tab

### Releases 💾
- Easiest way to get the game is from the releases page found [here](https://github.com/pixlbreaker/CSC290-Attach-4/releases)

- If not, you can download the github repository with the link below.

    ```bash
    $ git clone https://github.com/pixlbreaker/CSC290-Attach-4.git
    ```

### Downloading Python 🐍
This game uses python as the main language. In order to play you need to have python on your computer. Below we show you how to install `python 3.x`.

#### Windows
- Download python from their website linked [here](https://www.python.org/downloads/)

#### MacOS
- To install python on mac, you can use the homebrew to install the python package. To do so run the following command: 

    ```bash
    brew install python3
    ```

#### Linux
- For linux distributions such as Debian and Ubuntu, use the package manager system that comes with the system. For example:

    ```bash
    sudo apt-get install python3
    ```

### Downloading Dependancies
Alongside python, this project also uses a common library called pygame. Pygame is a library used to create games in python on any of the included operating systems. Since it does not require any other library in order to handle graphics rendering.

#### Pip
Pygame can be installed by using a package manager. The most commonly used one called `pip` is recommended in this case. If you downloaded python 3.4 or greated then pip is already on your system. 

*If not follow [this](https://pip.pypa.io/en/stable/installing/) recommended guide.*

#### Pygame
- Once pip is installed on your system, you can install pygame.
Run the following command to install pygame.

    ```bash
    pip install pygame
    ```

## Screenshots and Gameplay 👾
Here we have screenshots of the game in progress. 

![Screenshot_1](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/gameplay_1.png "Gameplay Picture 1")

![Screenshot_2](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/gameplay_2.png "Gameplay Picture 2")

![Gif1](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/Gif1.gif "Gif1")

![Gif2](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/Gif2.gif "Gif2")

## Documentation 📚

### Directory Structure
Our code is structured with the `main.py`, `README.md`, and `LICENSE.txt` at the root directory and the rest of the source code and assests can be found in the respective folders.

- `src`: Holds all the python modules to make the game
- `assets`: Holds all the assets for the game

### Code Structure

The code that resides in the `src` folder is broken up into the following files. Here are some of those files and the functionality of what those files do.

| File Name                      | Description           |  Lines |
| ------------------------------ |-----------------------|:------:|
| [AIPlayer.py](src/AIPlayer.py) | Holds the classes for the easy and hard AI. Each one is inherited from the abstract AIPlayer class.    | 134    |
| [board.py](src/board.py) | Here we have the class that holds the logic for the board. Some of the methods that are included check if the board is full. If a cell is valid and so on.    | 219   |
| [button.py](src/button.py) | Class that creates a button for the gui. Each button has a color, text, and font. Uses `Rect` class to create the button. | 86   |
| [gui.py](src/gui.py) | Holds all the visuals for the game. In the initializer we start the `init` function from the pygame module. Here we have the start game function and end game function.  | 106   |
| [inGame.py](src/inGame.py) | Creates all the buttons needed for the game. This class will do the following such as getting the colour of the button to the screen.  | 106   |

#### AI Functions

The below function is found in the [AIPlayer.py](src/AIPlayer.py) file. The function is called the decision_function. It is used by the AIHard to help determine where is the best possible spot to place down a chip. For a more detailed explanantion check the code comments in the helper functions listed below. In summary, the AIHard ```decision_function``` calls move_options (a method of the Board class) to get all the possible next moves given the current state of the board. The function computes a score for each column in the list "indices". A score is defined as the weighted sum of all adjacent paths (in any direction) of a given index in the board (check the helper function ```get_path_score``` for full details), where a path is defined as a contiguous line of common coloured discs. Then ```decision_function``` returns the highest scoring column, otherwise it returns the column closest to the median index of the board.

```python
if self.board.is_board_full() : return None

# get indices representing all next possible moves per column 
indices = self.board.move_options()

scores = {} 
for i in range(0, len(indices)):
    # populate scores dictionary with scores for every possible move
    scores.setdefault(indices[i], self.all_path_scores(indices[i]))
if len(scores) < 1 : return None

# return the highest scoring index
return self.interpret_scores(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))
```
## Extending the game
Some features of this game were out-of-scope due to our time frame. We encourage you add your own cool and exciting feature to make the game even more fun! Here are some examples:
### Creating new players
One way to add onto our game is by creating new types of players. This can be done by creating a sub class of the abstract Player class. All you have to do is implement the move method depending
on what kind of player you're trying to create. For example, you could make a player that will try to win only by getting 4 discs in a diagonal instead of a row or column. You would 
create an algorithm that tries to get 4 discs in a diagonal, and then add it to the move method.

### Adding a timed mode
Sometimes when playing Attach 4 with friends, they might take really long to decide where they want to make their move. A solution to this is creating a timed mode
where each player must make their move in a certain amount of time. If the player takes too long, then their turn could be skipped. The timer could start at the as soon
as the game is started and reset every time a player makes a move. It would make sense to implement this timer in gui.py or inGame.py as these classes deal with creating
the interface and continually updating it.

## Individual Contributions
### Michael Skotar
For this project my role was more administrative. I worked on the documentation, setting up the github repository and finding the license. I wanted the README.md to be the central location that held all the information for the project. This included installation, code structure, and dependancies.

As for the project I made small changes which included spelling errors or documentation. I also linked the AI modes to the existing project. Here I used the existing code as a guide to patch in the extra gamemodes.

### Michael De Lisio
My role in this project mostly entailed developing the logic and writing the code for the [AIPlayer.py](src/AIPlayer.py) module. This involved
developing a organized class structure that could easily interface with the gui, board and inGame modules. It also 
involved devising a reasonable strategy, within the alloted time and resources available, to develope a fun and competitive
artificial player to play against.

Since, as a group we decided to mostly use object oriented programming structure, I followed this model for consistency and
so that each module could interface more seemlessly with each other. The AIPlayer abstract class defines an abstract method ```decision_function```, which determines the AIPlayer's (of some difficulty level) next move; specifically, it determines
and returns a valid index into the board matrix (a tuple of integers representing a row and column respectively) based on
some algorithm. 

The AIEasy and AIHard difficulty levels both implemented different decision functions. AIEasy implements the decision function
using random number generation. AIHard's implementation is a little more intuitive. The inspiration for this game, "Connect 4", has a known solution that involves generating all possible moves and scoring them accordingly. This known solution, was neither within the scope of our implementation or resources to attempt. Therefore, the AIHard uses an adaptation of this solution to implement its ```decision_function```. I wrote a more detailed summary of the AIHard algorithm used in the "AI Functions" section within this file. Other than the implementation of the [AIPlayer.py](src/AIPlayer.py) module, my influence on other modules was 
limited (this was agreed upon by design) and my contributions to this README.md document was soley to the "AI Functions"
section, since we assigned a group responsible for the administrative tasks such writing the README.md, licensing, etc.

### Niral Patel
In this project, I was responsible for creating the architecture for all the players, as well as implementing the PlayerHuman class. 
I decided to first create an abstract class called Player. This class has an unimplemented move method which sub classes of Player should implement. 
This class also contained implemented methods like get_color() since the implementation of this method would be the same for all player types.
I then implemented this abstract class by creating the PlayerHuman class. This sub class implemented the move method and could now be initialized. 
The architecture of implementing an abstract class was then used by another group member to create the AI players. I also contributed to README.md 
by giving examples of how to extend our game.

### Tomasz Cieslak
I primarily contributed to the creation of the [board.py](src/board.py), as well as the refactoring of the game [gui.py](src/gui.py). The board class is essential in order to create and edit the game board. The refactoring of the GUI allowed us to more easily implement the features we plan on adding, instead of implementing all our code in one large ``` .py``` file.

My [board.py](src/board.py) implementation allows us the ability to drop pieces, check if the game has ended and other various methods that are useful to comunicate with the game board. Some methods that I created include: ```drop_piece```, ```check_connected```, ```drop_piece```,  ```is_full```, etc. This class is essential in order to create a fully functional board game.

The GUI refactoring allowed my team to better use object oriented programming, where buttons and other features can more easily be implemented. This refactoring split up our previous gui into 3 new class files, which now include: [gui.py](src/gui.py), [inGame.py](src/inGame.py) and [mainMenu.py](src/mainMenu.py). This refractoring of code is convenient since it allows us to more easily implement the features we require.

### Ravnit Lotay
My role for this project concentrated primarily on the visual aspect of the game. I designed the initial gui in gui.py, then
recieved assistance from a fellow groupmate to further developing the gui. Initially, I created a basic gui with a simple screen, board, and player tokens,
however, when I began thinking about more complex aspects of the gui, I realized I would need help. The first realization occured while working with pygame 
as it was more complex than I initally thought. Because of the complexity, I decided to redo the gui in a more simplistic way, using pygame more effectively.
After redoing the gui, the visual aspect was greatly improved and add functionality was added for playback. After redoing the board, however, I was met with the
issue of adding game modes such as player vs player and player vs ai, so I asked for assistance from another groupmate. Once my groupmate finished his improvements
to the gui, I made minor adjustments to the new files to improve overall design and structure. 

As for README.md, I contributed by providing gif's of the game's playback for both Player vs Player and Player vs AIHard. My contributions to README.md
were minimal as a single group member focused on the administrative aspect of the project, including README.md

## Additional Information

- **License**: Uses the MIT License, which can be found at the [LICENSE.txt](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/LICENSE.txt)
- **Contribute**: If you would like to contribute please make a Pull Request