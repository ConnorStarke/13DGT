from tkinter import *

# Create a window
root = Tk()
root.title("Connors Comics")

label1 = Label(root, text="Connors Comics",
wraplength=100, justify="center", fg="Red", bg="Gray")
label1.pack()

label2 = Label(root, text="This is the start of my GUI project!", wraplength=100, justify="left", fg="black", bg="yellow")
label2.pack()

# Run the main window loop
root.mainloop ()
