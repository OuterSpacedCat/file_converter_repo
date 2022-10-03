import pandas as pd
import numpy as np
import csv
import glob
import re
import string 
import csv
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def string_in_file(file):
    datContent = [i.strip().split('\t') for i in open(r"f'{file}").readlines()]
    with open(file,'w') as F:
        F.rename(F.with_suffix(".csv"))
        writer = csv.writer(F)
        writer.writerows(datContent)
        return datContent

def handle_keypress(event):
    print(event.char)
    if event.type == "keypress":
        handle_keypress(event)


def handle_click():
    click_event = Label(window, text = 'Uploaded!')
    click_event.pack()

def retrieve_input():
    fpath = InputFile.get()
    note = label(ws, text = f'{fpath} uploaded!', pady =20, bg = 'skyblue')
    note.pack()
    user_entry = self.InputFile.get("1.0", 'end-1c')
    print(note)



#window attributes

window = tk.Tk()
window.geometry('300x200')
window.resizable(False, False)
window.title("File Converter")
direction = tk.Label(text = "Please paste the full filepath to your IC file (.dat)", anchor = CENTER)
InputFile = tk.Entry().place(x = 40, y = 115)
button1 = tk.Button(window, text = "Submit", command = handle_click)
button1.place(x =220,y= 110)
greeting = tk.Label(
    text = "Welcome to the file converter!",
    foreground = "White",
    background = "purple",
    width = 30,
    height = 5
    
)


greeting.pack()
direction.pack()
#button1.pack()
window.bind("<Key>", handle_keypress)

window.mainloop()


