import json
import os
import sys

import curses

from cursesshortcuts import draw_borders, draw_box_borders

# Deal with being unable to import curses on windows because it doesnt work properly by default
try:
    import curses
except ModuleNotFoundError:
    print("Could not import curses. If you are running on windows please install the 'windows-curses' module")
    sys.exit(1)

# This wont work from an ide shell so deal with that
try:
    screen = curses.initscr()
except ModuleNotFoundError:
    print("could not create screen. This is most likely because you are"
          "running from an IDE shell and not a terminal. Please run this"
          "program from a terminal")
    sys.exit(1)

# Min terminal height needed to run this program without issues
term_height = os.get_terminal_size().lines
term_width = os.get_terminal_size().columns
if term_height < 35 or term_width < 120:
    print(f"Terminal height must be at least 120x35 (currently {term_width}x{term_height})")

term_height = os.get_terminal_size().lines
term_width = os.get_terminal_size().columns
curses.start_color()

curses.curs_set(False)
screen.keypad(True)
curses.noecho()
draw_borders(screen)
draw_box_borders(screen, curses)
screen.addstr(5, 110, 'hello :3')










while True:
    if screen.getch() == 10: break



