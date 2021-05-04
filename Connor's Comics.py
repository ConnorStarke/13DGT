#Imports
from tkinter import *
from tkinter import ttk
import random

#Class Code
#Functions and Setup 
#GUI Code

root = Tk()
root.title("Comical Comics")
words = StringVar()
 
#Left Frame
left_frame = ttk.LabelFrame(root, text=" SELL ")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

#Creating the Dropdown Menu
chosen_option = StringVar()
options = ['Super Dude', 'Lizard Man', 'Water Woman']
option_menu = ttk.OptionMenu(left_frame, chosen_option, options[0], *options)
option_menu.grid(row=1, column=0, padx=10, pady=10)


#Right Frame
right_frame = ttk.LabelFrame(root, text=" STOCK ")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

#Setting the Message Text Variable
Stock_text = StringVar()
Stock_text.set("Da Comics")

#Packing the Message Label
message_label = ttk.Label(right_frame, textvariable=Stock_text, wraplength=250)
message_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#Bottom Frame
L_inside_frame = ttk.LabelFrame(root, text="TEXT")
L_inside_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="SNEW")

#Settinging the Message Text Variable
bottom_text = StringVar()
bottom_text.set("Connor Starke 2021 CC")

#Pack the Message Label
message_label = ttk.Label(L_inside_frame, textvariable=bottom_text, wraplength=250)
message_label.grid(row=5, column=0, padx=10, pady=10)
