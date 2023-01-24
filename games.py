import tkinter
import random

hod_man = 0
hod_comp = 0

def click_stone():
    hod_man = 1
    hod_comp()
    
def click_scissors():
    hod_man = 2
    hod_comp()
    
def click_paper():
    hod_man = 3
    hod_comp()
    
def hod_comp():
    hodComp = random.randint(1, 3)
    print(hodComp)
    if hodComp == 1:
        btnComp.config(image=img1)
    elif hodComp == 2:
        btnComp.config(image=img2)
    else:
        btnComp.config(image=img3)

win = tkinter.Tk()
win.geometry("600x600")

lblScoreComp = tkinter.Label(text="0")
lblScoreComp.place(x=20, y=20)

lblScoreMan = tkinter.Label(text="0")
lblScoreMan.place(x=200, y=20)

img1 = tkinter.PhotoImage(file="images/img1.png")
btnStone = tkinter.Button(image=img1, command=click_stone)
btnStone.place(x=300, y=100)

img2 = tkinter.PhotoImage(file="images/img2.png")
btnScissors = tkinter.Button(image=img2, command=click_scissors)
btnScissors.place(x=300, y=200)

img3 = tkinter.PhotoImage(file="images/img3.png")
btnPaper = tkinter.Button(image=img3, command=click_paper)
btnPaper.place(x=300, y=300)

btnComp = tkinter.Button(image=img3)
btnComp.place(x=10, y=200)

win.mainloop()