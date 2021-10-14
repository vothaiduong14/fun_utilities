import tkinter as tk
import random

width = 600
height = 400
title = 'Roll Dice App'
button_text = 'roll_dice'
button_color = 'green'

# set main frame
main_frame = tk.Tk()
main_frame.geometry(f'{width}x{height}')
main_frame.title(title)

# set display box for our dice:
display_box = tk.Label(main_frame, text = '', font = ('Helvetica', 160))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    roll_outcome = random.choice(dice)
    display_box.configure(text = f'{roll_outcome}')
    display_box.pack()

# set button
button = tk.Button(main_frame, text = button_text, foreground = button_color, command = roll_dice)
button.pack()

# call and keep the window open
main_frame.mainloop()