from tkinter import *

root = Tk()

logo = PhotoImage(file="logo.png")
logo_label = Label(root, image=logo)
logo_label.pack()

root.mainloop()
