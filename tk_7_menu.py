from tkinter import *

def new_file():
    print("Function new_file is called!")

def save_file():
    print("Function save_file is called!")

def copy():
    print("Function copy is called!")

def paste():
    print("Function paste is called!")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

root.mainloop()
