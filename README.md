# CSC290 - Attach 4

## Content
1. Introduction
2. How to Play
3. Installation
4. Screenshots
5. Documentation
6. Individual Contributions
7. Additional Information

## Introduction
This is a connect-4 inspired game built with python and pygame for our **CSC 290: Communication Skills for Computer Scientists**. Our team members include:

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

- If not you can download the github repository with the above link.

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
- For linux distributions, such as Debian and Ubuntu use the package manager system that comes with the system. For example:

    ```bash
    sudo apt-get install python3
    ```

### Downloading Dependancies
Alongside python, this project also uses a common library called pygame. Pygame is a library used to create games in python on any of the included operating systems. Since it does not require any other library in order to handle graphics rendering.

#### Pip
Pygame can be installed by using a package manager. The most commonly used one called `pip` is recommended in this case. If you downloaded python 3.4 or greated then pip is already on your system. 

*If not follow [this](https://pip.pypa.io/en/stable/installing/) recommended guide.*

#### Pygame
- Once pip is now installed on your system you can install pygame.
Run this following command to install pygame.

    ```bash
    pip install pygame
    ```

## Screenshots 👾
Here we have screenshots of the game in progress. 

![Screenshot_1](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/gameplay_1.png "Gameplay Picture 1")

![Screenshot_2](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/assets/screenshots/gameplay_2.png "Gameplay Picture 2")

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

The below function is found in the [AIPlayer.py](src/AIPlayer.py) file. The function is called the decision_function. It is used by the HardAI to help determine where is the best possible spot to place down a chip.

```python
if self.board.is_board_full():
    return None

# Scores and Indicies
indices = self.board.move_options()
scores = {}

for i in range(0, len(indices)):
    scores.setdefault(indices[i], self.all_path_scores(indices[i]))
if len(scores) < 1 : 
    return None
print("Scores: " +str(scores))

# Returns the interperted scores that is sorted
return self.interpret_scores(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))
```

## Individual Contributions
### Michael Skotar
For this project my role was more administrative. I worked on the documentation, setting up the github repository and finding the license. I wanted the README.md to be the central location that held all the information for the project. This included installation, code structure, and dependancies.

As for the project I made small changes which included spelling errors or documentation. I also linked the AI modes to the existing project. Here I used the existing code as a guide to patch in the extra gamemodes.


## Additional Information

- **License**: Uses the MIT License, which can be found at the [LICENSE.txt](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/LICENSE.txt)
- **Contribute**: If you would like to contribute please make a Pull Request