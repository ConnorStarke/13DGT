# 13DGT
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My GUI App")


button1 = ttk.Button(root, text="Row 0, Col 0")
button1.grid(row=0, column=0, sticky="WE", columnspan="7")

button4 = ttk.Button(root, text="Row 1, Col 0")
button4.grid(row=1, column=0)

button5 = ttk.Button(root, text="Row 2, Col 0")
button5.grid(row=2, column=0)
button5 = ttk.Button(root, text="Row 3, Col 0")
button5.grid(row=3, column=0)
button5 = ttk.Button(root, text="Row 4, Col 0")
button5.grid(row=4, column=0)
button5 = ttk.Button(root, text="Row 5, Col 0")
button5.grid(row=5, column=0)
button5 = ttk.Button(root, text="Row 6, Col 0")
button5.grid(row=6, column=0)

button8 = ttk.Button(root, text="Row 1, Col 1")
button8.grid(row=1, column=1, columnspan=5, rowspan=5 ,sticky="NSWE")


root.mainloop()
