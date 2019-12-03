# CSC290 - Attach 4

## Content
1. Introduction
2. How to Play
3. Installation
4. Screenshots
5. Documentation
6. Additional Information

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
This is a turn-based game, meaning that each player has a turn when they make their move. Each move consists of selecting a row to drop a chip in.

In this specific implementation we use mouse's position to determine where to drop the chip.

## Installation 🖥️
Our game relies on both python and pygame. Python is the programming language that our game was coded in, while pygame is the package we used to have a graphical user interface.

### Downloading Python 🐍
#### Windows
- Download python from their website linked [here](https://www.python.org/downloads/)

#### MacOS
- To install python on mac, you can use the homebrew to install the python package. To do so run the following command: 

    `brew install python3`

#### Linux
- For linux distributions, such as Debian and Ubuntu use the package manager system that comes with the system. For example:

    `sudo apt-get install python3`

### Downloading Dependancies
Alongside python, this project also uses a common library called pygame. Pygame is a library used to create games in python on any of the included operating systems. Since it does not require any other library in order to handle graphics rendering.

#### Pip
Pygame can be installed by using a package manager. The most commonly used one called `pip` is recommended in this case. If you downloaded python 3.4 or greated then pip is already on your system. 

*If not follow [this](https://pip.pypa.io/en/stable/installing/) recommended guide.*

#### Pygame
- Once pip is now installed on your system you can install pygame.
Run this following command to install pygame.

    `pip install pygame`

### Releases
- Easiest way to get the game is from the releases page found [here](https://github.com/pixlbreaker/CSC290-Attach-4/releases)

## Screenshots 👾

## Documentation 📚

### Directory Structure
Our code is structured with the `main.py`, `README.md`, and `LICENSE.txt` at the root directory and the rest of the source code and assests can be found in the respective folders.

### Code Structure

## Additional Information

- **License**: Uses the MIT License, which can be found at the [LICENSE.txt](https://github.com/pixlbreaker/CSC290-Attach-4/blob/master/LICENSE.txt)
- **Contribute**: If you would like to contribute please make a Pull Request