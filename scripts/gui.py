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

root = Tk()
root.geometry('300x200')
root.resizable(False, False)

#icons
root.iconbitmap("C:\\Users\\padams\\Desktop\\Porsche\\git_projects\\file_converter\\GUI\\white_logo.ico")
img = PhotoImage(file = r"C:\Users\padams\Desktop\Porsche\git_projects\file_converter\GUI\arrow-next-2825.png")

#conn = sqlit3.connect('')
#c = conn.cursor()

def query():
    c.execute("SELECT site_id, site_name, UWI FROM delivery.cd_site")
    well_names = c.fetchall()
    for wells in well_names:
        pd.merge(well_names, df, on = "Well")
        
def retrieve_input():
    fpath = user_entry_window.get()
    print(fpath)
    Label(root, text = f'{fpath}, uploaded!', pady =20, bg = 'skyblue')

def handle_click():
    click_event = Label(root, text = "Uploaded").place(x = 80,y = 160)
    fpath = user_entry_window.get()
    button_pressed.set("button_pressed")
    
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def popup():
    messagebox.showinfo("Information", "This GUI will convert your files from one format to another. Please select the file origin and destination software along with the file path and click submit.")

def origin_selection(selection):
    choice1 = selection
    print(selection)
    return choice1
    
def destination_selection(selection2):
    choice2 = selection2
    print(selection2)
    return choice2
    
def ic_to_kingdom(file):
    fpath = user_entry_window.get()
    print("this function is bananas")
    datContent = [i.strip().split('\t') for i in open (fr'{fpath}').readlines()]
    with open(datContent,'w') as F:
        F.rename(F.with_suffix(".csv"))
        writer = csv.writer(F)
        writer.writerows(datContent)
        return datContent

button_pressed = StringVar()    
#def button_pressed():
#    button_pressed.set("button_pressed")
    
#text    
greeting = Label(root, text = "Welcome to the file converter!", foreground = "white", background = "purple").place( x = 60, y = 0)
select_orig_software = Label(root, text = "Input File").place(x = 30, y = 50)
select_dest_software = Label(root, text = "Output File").place(x = 160, y = 50)
directions = Label(root, text = "Please paste the full path to your IC file (.dat)").place(x = 30,y = 20)
#input fields
orig_menu = StringVar()
orig_menu.set("File origin")
dest_menu = StringVar()
dest_menu.set("File destination")

user_entry_window = Entry(root, width = 30)
user_entry_window.place(x = 40, y = 135)

o_select = OptionMenu(root, orig_menu, "IC","Kingdom","Petrel","WellCAD","ArcGIS Pro", command = origin_selection).place(x = 30, y = 70)
d_select = OptionMenu(root, dest_menu, "IC","Kingdom","Petrel","WellCAD","ArcGIS Pro", command = destination_selection).place(x = 160, y = 70)
arrow = Label(root,image = img).place(x = 130, y = 70)
button1 = Button(root, text = "Submit", command = combine_funcs(handle_click,retrieve_input,button_pressed))
button1.place(x = 230, y=132)
button2 = Button(root, text = "Info", command = popup).place(x = 260, y = 170)

button1.wait_variable(button_pressed)


#conversion zone
if choice1 == "IC" and selection2.get() == "Kingdom":
    df = ic_to_kingdom(fpath)
    df = pd.DataFrame.from_records(datContent)
    df=df.loc[7:]
    df.columns=df.loc[7]
    df=df.loc[8:].reset_index(drop=True)
#df.columns = ['Well','Top_Depth','Base_Depth',"namey"]
    df.head(15)
#dfs = pd.DataFrame.from_records(datContent)


root.mainloop()
#conn.close()
