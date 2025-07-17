import tkinter as tk
from tkinter import Menu

def new_file():
    print("New File created!")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Francis TUrbine")

# Create t
menubar = Menu(root)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: print("This is a demo app"))
menubar.add_cascade(label="Help", menu=help_menu)

# Attach the menu bar to the window
root.config(menu=menubar)

root.mainloop()