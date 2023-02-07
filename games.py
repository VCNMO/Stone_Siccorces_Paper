import tkinter
import random

STONE = 1
PAPER = 2
SCISSORS = 3

hod_man = 0
hod_comp = 0
score_man = 0
score_comp = 0

def change_score():
    global score_man, score_comp
    if hod_man == STONE: #камень
        if hod_comp == PAPER: # бумага
            score_comp = score_comp + 1
        elif hod_comp == SCISSORS: # ножницы
            score_man = score_man + 1
    elif hod_man == PAPER:
        if hod_comp == STONE:
            score_man = score_man + 1
        elif hod_comp == SCISSORS:
            score_comp = score_comp + 1
    elif hod_man == SCISSORS:
        if hod_comp == STONE:
            score_comp = score_comp + 1
        elif hod_comp == PAPER:
            score_man = score_man + 1
            
    lblScoreComp.config(text=score_comp)
    lblScoreMan.config(text=score_man)    

def click_stone():
    global hod_man
    hod_man = 1
    do_hod_comp()
    change_score()
    
def click_scissors():
    global hod_man
    hod_man = 2
    do_hod_comp()
    change_score()
    
def click_paper():
    global hod_man
    hod_man = 3
    do_hod_comp()
    change_score()
    
def do_hod_comp():
    global hod_comp
    hod_comp = random.randint(1, 3)
    if hod_comp == 1:
        btnComp.config(image=img1)
    elif hod_comp == 2:
        btnComp.config(image=img2)
    else:
        btnComp.config(image=img3)

win = tkinter.Tk()
win.title("Камень - Ножницы - Бумага")
win.geometry("400x400")

lblComp = tkinter.Label(text="ИГРАЕТ КОМПЬЮТЕР")
lblComp.place(x=20, y=20)

lblScoreComp = tkinter.Label(text="0")
lblScoreComp.place(x=20, y=50)

lblMan = tkinter.Label(text="ИГРАЕТ ЧЕЛОВЕК")
lblMan.place(x=200, y=20)

lblScoreMan = tkinter.Label(text="0")
lblScoreMan.place(x=200, y=50)

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
btnComp.place(x=30, y=200)

win.mainloop()