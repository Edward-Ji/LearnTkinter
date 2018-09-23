from tkinter import *

root = Tk()

label1 = Label(root, text="default pack", bg="red", fg="white")
label1.pack()
label2 = Label(root, text="fill X", bg="green", fg="black")
label2.pack(fill=X)
label3 = Label(root, text="fill Y", bg="blue", fg="black")
label3.pack(side=LEFT, fill=Y)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="button1", fg="red")
button2 = Button(topFrame, text="button2", fg="yellow")
button3 = Button(topFrame, text="button3", fg="green")
button4 = Button(bottomFrame, text="button4", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()
