from tkinter import *

root = Tk()

def left_click(event):
    print("left click button")

def middle_click(event):
    print("middle click button")

def right_click(event):
    print("right click button")

frame = Frame(root, width=800, height=600)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()

root.mainloop()
