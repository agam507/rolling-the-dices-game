# dice_game.py

from tkinter import *
import random

# Create the main window
window = Tk()
window.configure(bg="black")
window.geometry("480x360")
window.title("Rolling The Dices Game")
window.resizable(0, 0)

# Dice Unicode Characters
dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

# Function to roll the dice
def roll_dices():
    dice1 = random.choice(dice_dots)
    dice2 = random.choice(dice_dots)
    label.config(text=f'{dice1}{dice2}')

# Roll Button
roll_button = Button(window, text="Roll",
                     width=10, height=2,
                     font=15, fg="white", bg="#36454f",
                     bd=2, command=roll_dices)
roll_button.pack(padx=10, pady=15)

# Dice Display Label
label = Label(window, font=("times", 150), bg="black", fg="aqua")
label.pack()

# Start the GUI loop
window.mainloop()
