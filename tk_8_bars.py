from tkinter import *

num = 1

# ***** Menu *****
def new_file():
    print("Function new_file is called!")

def save_file():
    print("Function save_file is called!")

def copy():
    print("Function copy is called!")

def paste():
    print("Function paste is called!")

def insert_img():
    print("Function insert_img is called!")

def move_img():
    print("Function move_img is called!")

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

# ***** Tool Bar *****
toolbar = Frame(root, bg="blue")

insert_butt = Button(toolbar, text="Insert Image", command=insert_img)
insert_butt.pack(side=LEFT, padx=2, pady=2)
move_butt = Button(toolbar, text="Move Image", command=move_img)
move_butt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****
status = Label(root, text="Status bar shows here!", bd=2, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# ***** Run *****
root.mainloop()
