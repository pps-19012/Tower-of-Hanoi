# Tower of Hanoi game
The main file to run is tower_of_hanoi.py. 
There is another file instructions.py, which can be opened by a 'How to Play' button which you will see in main file.
Instructions on how to play the game will show when instructions.py file is run.

## Libraries used are tkinter and Pillow.
tkinter is pre-installed with python but you have to install Pillow.
To install, type in command prompt:
```bash
pip install Pillow
```
## Also, to access instructions.py from tower_of_hanoi.py, I have used:
```bash
import os
....
def help() :
    os.system('python instructions.py')
```
This should work in most of the operating systems.
