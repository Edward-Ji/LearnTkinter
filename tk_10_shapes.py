from tkinter import *

root = Tk()

def del_red_line():
    canvas.delete(red_line)

def del_all():
    canvas.delete(ALL)

def restore():
    global black_line, red_line, green_box
    black_line = canvas.create_line(10, 10, 190, 80)
    red_line = canvas.create_line(10, 80, 190, 150, fill="red")
    green_box = canvas.create_rectangle(25, 25, 80, 60, fill="green")

restore_butt = Button(root, text="restore all", command=restore)
restore_butt.pack()
delete_butt = Button(root, text="delete red line", command=del_red_line)
delete_butt.pack()
delall_butt = Button(root, text="delete all", command=del_all)
delall_butt.pack()

canvas = Canvas(root, width=200, height=160)
canvas.pack()
restore()

root.mainloop()
