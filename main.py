"""
=== Module description ===
The main.py file general job is to define the entry point
for the execution path of the Attach 4 game. The init() function
is called upon execution of this file, which initializes a GUI
object and displays the main screen (which starts the games loop).
"""
# Import classes from project files
from src.gui import Gui

# Initializes the entry point of the Attach 4 game
if __name__ == "__main__":
    Gui()
