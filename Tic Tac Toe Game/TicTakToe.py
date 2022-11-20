from tkinter import *
import random
#import numpy as np

counter = 0

#Game = np.zeros((3,3))
Game = [[0,0,0],[0,0,0],[0,0,0]]
#print(Game)

windows = Tk()
windows.title("Tic Tac Toe Game")
entrya = Label(windows,text= "What is Player 1 Name? ", font=40)
entrya.grid(row=0, column=0)
entryA = Entry(windows)
entryA.grid(row=0,column=2)

entryb = Label(windows,text = "What is Player 2 Name? ", font=40)
entryb.grid(row=1,column=0)
entryB = Entry(windows)
entryB.grid(row=1,column=2)

def newgame ():
    pass
    
def gamewindow():
    global counter
    if counter <1:
        Player2 = entryB.get()
        Player1 = entryA.get()
        randplayer = [Player1, Player2]
        Pl_choice = random.choice(randplayer)

        win = Toplevel(windows)
        win.title("Tic Tac Toe")
        sent2 = Label(win,text= Pl_choice + " Turn", font=40)
        sent2.pack()
        reset = Button(win,text= " Restart Game", font = 40, command = newgame())
        reset.pack()
        counter = counter + 1

        win.mainloop()
    

gamest = Button(windows,text= "Start Game", font = 40, command = gamewindow)
gamest.grid(row=2, column =1)


                



windows.mainloop()
