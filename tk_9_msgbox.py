from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()

answer = msgbox.askquestion("Question", "Are you under 18 years old?")

if answer == "yes":
    msgbox.showinfo("Alert", "This game is violent!")
elif answer == "no":
    msgbox.showinfo("Tips", "You are able to access the content")

root.quit()
