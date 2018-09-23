from tkinter import *

root = Tk()

def func():
    print("Function func is called!")

button_1 = Button(root, text="button_1", command=func)
button_1.pack()

root.mainloop()
