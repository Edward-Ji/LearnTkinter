from tkinter import *

class Clickables:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button_print = Button(frame,
                                   text="print",
                                   command=self.print_msg)
        self.button_print.pack(side=LEFT)

        self.button_quit = Button(frame,
                                  text="quit",
                                  command=frame.quit)
        self.button_quit.pack(side=LEFT)

    def print_msg(self):
        print("This is a message!")

root = Tk()
clickables = Clickables(root)
root.mainloop()
