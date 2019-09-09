import sys
from tkinter import *
win = Tk()
win.title("Character checker")
win.resizable(False, False)
win.geometry("640x480")
Label(win, text="Type in the string!", font=("Monaco", 40, "bold")).pack()
txt = StringVar()
lbl = StringVar()
entryBox = Entry(win, textvariable=txt, font=("Helvetica", 20, "normal")).pack()
updatedLabel = Label(win, textvariable=lbl, font=("Times", 30, "italic"), fg="Green").pack()
def Refresh():
    lbl.set("Number of Characters: {}".format(len(txt.get())))
    win.after(1, Refresh)
Refresh()
win.mainloop()

#while True:
#print(entryBox.values)
print(len(txt.get()))

def challenge1():
    txt = input("What is the input string? ")
    while txt == "":
        txt = input("Please type in something! ")
    print("{} has {} characters. ".format(txt, len(txt)))

