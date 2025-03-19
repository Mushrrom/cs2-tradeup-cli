import json
import os
import sys

import curses

from cursesshortcuts import draw_borders, draw_box_borders, draw_text
from gen_colors import gen_colors
from text_entry import search_item
from search_items import generate_matrix

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
    quit()

# Curses colour stuff
curses.start_color()
gen_colors(curses)
curses.init_pair(1, 1, 0) # default text
curses.init_pair(2, 0, 1) # Inverted from default

# Curses config
curses.curs_set(False)
screen.keypad(True)
curses.noecho()

# Initial setup
draw_borders(screen)
draw_box_borders(screen, curses)
matrix, vectorizer = generate_matrix() 
screen.addstr(5, 110, 'hello :3')

current_selection = 1
box_selection = 0

selected_items = ['woahg', 'woahj', '', '', '', '', '', '', '', '', '']
float_values = [0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035]
# main loop
while True:
    draw_text(screen, curses, selected_items, current_selection, float_values)
    key = screen.getch()
    screen.addstr(35, 2, str(key) + "####")

    match key:
        case 9: # tab
            current_selection = current_selection+1 if current_selection != 10 else 1
            box_selection = 0
            # draw_text(screen, curses, selected_items, current_selection, float_values)
        case 351: # shift+tab
            current_selection = current_selection-1 if current_selection != 1 else 10
            box_selection = 0
        
        case 10:
            if box_selection == 0:
                selected_items[current_selection] = search_item(screen, curses, selected_items[current_selection], current_selection, matrix, vectorizer)
        
    

        # case
    
    # screen.addstr(1, 0, "asd", 2)



