# import tkinter (for window)
from tkinter import *
import tkinter as tk
import os
import random

# Some default vars
root = tk.Tk()
color = "grey"
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

# Window details
root.title("Password Generator")
root.geometry("600x400")
root.resizable(height=False, width=False)
root.iconphoto(False, tk.PhotoImage(file='lock.ico'))

# canvas (grey block)
canvas = tk.Canvas(root, height=375, width=575, bg=color)
canvas.place(x=10, y=10)

# Output label so people see the output, works because not packet yet
OutLabel = Label(root)


def UpdateOutput():
    OutLabel.config(text=Output, font=('Display', 7))


# Global vars + default output they have + updates output
password = 'Click "Generate" to generate a password, and move the scroller to change its lengh'
lengh = 1
Output = password
UpdateOutput()


# Scale number appearing  and updates variables
Scaler = tk.Label(root, bg="white", fg="black")
scale_val = "Characters in password= 1"
Scaler.config(text=scale_val)


def get_value(x):
    scale_val = "Characters in password= " + str(x)
    Scaler.config(text=scale_val)
    global lengh
    lengh = int(x)
    Scaler.place(x=210, y=180)


# The scale itself
v1 = DoubleVar()
Scale = tk.Scale(root, variable=v1, from_=1, to=100,
                 orient=HORIZONTAL, command=get_value, width=20, length=300)
Scale.place(x=145, y=200)

# permission to copy, if false will output no perm to copy
AllowCopy = False


# label for how strong password is:
HowPower = tk.Label(root, font=('Display', 15), bg=color)


def UpdateHowPower():
    strong = 'Bad', 'red'
    if lengh >= 9:
        strong = 'Weak', 'orange'
    if lengh >= 15:
        strong = 'Good', 'yellow'
    if lengh >= 30:
        strong = 'Awesome!', '#66ff66'
    if lengh >= 60:
        strong = 'LEGENDARY', '#00cc00'
    if lengh == 100:
        strong = 'UNBREAKABLE!!', '#009933'
    HowPower.config(text=strong[0], bg=strong[1])


# button to generate + output updation


def Generate():
    global password
    password = ''
    for c in range(lengh):
        password += random.choice(chars)
    global Output
    Output = password
    UpdateOutput()  # Updates output
    UpdateHowPower()  # Updates how powerful the password is

    global AllowCopy
    AllowCopy = True


GenerateButton = tk.Button(root, text="Generate", padx=10,
                           pady=5, fg=color, bg="#ffffff", command=Generate)
GenerateButton.place(x=145, y=140)


# button to copy to clipboard + output updation
def copy():
    global Output
    if AllowCopy == True:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        Output = "Copied: " + password
        UpdateOutput()
    else:
        Output = "Please Generate a password first"
        UpdateOutput()


CopyB = tk.Button(root, text="Copy to Clipboard", padx=10,
                  pady=5, fg=color, bg="#ffffff", command=copy)
CopyB.place(x=325, y=140)

# Exit Button


def ExitC():
    exit()


ExitB = tk.Button(root, text="Exit", padx=10, pady=5,
                  fg=color, bg="#ffffff", command=ExitC)
ExitB.place(anchor='nw')


# label that warns about clipboard
WarningC = tk.Label(
    root, text='If you clicked on "Copy to Clipboard" what you copied will go away if you close the program', bg=color)
WarningC.place(y=360, x=50)

# Label Title
Title = tk.Label(root, font=('Display', 30),
                 text="Password Generator", bg=color)
Title.place(x=115, y=50)

# adds the updated lable, and updated power in the end, and scaler
OutLabel.place(y=260, anchor='center', bordermode=OUTSIDE, x=300)
HowPower.place(y=300, anchor='center', bordermode=OUTSIDE, x=300)
Scaler.place(x=210, y=180)

# main loop
root.mainloop()