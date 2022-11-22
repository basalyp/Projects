from tkinter import *
import random
#import numpy as np

counter = 0
randplayer=[]
Plturn = 0

#Game = np.zeros((3,3))
Game= [[0,0,0],[0,0,0],[0,0,0]]
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

def emptyspace():
    EmptySpaces = True
    for row in range(3):
        for column in range(3):
            if Game[row][column]['text'] == "":
                EmptySpaces = True
            else:
                EmptySpaces = False
    return EmptySpaces
def checkwinner():
    for row in range (3):
        if Game[row][0]['text'] == Game[row][1]['text'] and Game[row][1]== Game[row][2]['text'] != "":
            return True
    for column in range(3):
        if Game[0][column]['text'] == Game[1][column]['text'] and Game[1][column]== Game[2][column]['text']!="":
            return True
    if (Game[0][0]['text'] == Game[1][1]['text']== Game[2][2]['text']) or (Game[2][0]['text'] == Game[1][1]['text']== Game[0][2]['text'])!= "":
        return True
    elif emptyspace() is False:
        return "TIE"
    else:
        return False
        
    return False

    pass

def next_turn(row,column):
    global Plturn
    global randplayer
    if Game[row][column]['text']== "" and checkwinner() is False: #Access the text of the Button
        if Plturn == randplayer[0]:
            Game[row][column]['text']=randplayer[0]
            if checkwinner() is False:
                Plturn = randplayer[1]
                label.config(win, text=randplayer[0]+ "turn")
            elif checkwinner() is True:
                win3 = Toplevel(win)
                win3.title("Winner Winner CHicken Dinner")
                winner1 = Label (text="Winner Winner Chicken Dinner")
                winner1.pack()
            elif checkwinner() == "TIE":
                win3 = Toplevel(win)
                win3.title("OH NOOOO IT IS A TIE :(")
                winner1 = Label (text="ON NO IT IS A TIE, Never seen an equally matched skilled opponent in my life ")
                winner1.pack()
                Plturn = randplayer[0]
                
            
        else:
            Game[row][column]['text']=randplayer[1]
            if checkwinner() is False:
                Plturn= randplayer[0]
                label.config(win,randplayer[1] + 'turn')
            elif checkwinner() is True:
                win3 = Toplevel(win)
                win3.title("Winner Winner CHicken Dinner")
                winner1 = Label (text="Winner Winner Chicken Dinner")
                winner1.pack()
                Plturn = randplayer[0]
            elif checkwinner() == "TIE":
                win3 = Toplevel(win)
                win3.title("OH NOOOO IT IS A TIE :(")
                winner1 = Label (text="ON NO IT IS A TIE, Never seen an equally matched skilled opponent in my life ")
                winner1.pack()
                Plturn = randplayer[0]
                
        
    pass

    
def gamewindow():
    global counter  #To Modify variable outsideof scope
    global randplayer
    global Plturn
    if counter <1:
        Player2 = entryB.get()
        Player1 = entryA.get()
        randplayer = [Player1, Player2]
        Pl_choice = random.choice(randplayer)
        Plturn = Pl_choice

        win = Toplevel(windows)
        win.title("Tic Tac Toe")
        sent2 = Label(win,text= Pl_choice + " Turn", font=40)
        sent2.pack()

        frame = Frame(win)
        frame.pack()
        
        for row in range(3):
            for column in range(3):
                Game[row][column]=Button(frame,text="", width=20, height = 10, command = next_turn(row,column))
                Game[row][column].grid(row=row,column=column)
                
        reset = Button(win,text= " Restart Game", font = 40, command = newgame())
        reset.pack()
        counter = counter + 1

        win.mainloop()
    

gamest = Button(windows,text= "Start Game", font = 40, command = gamewindow)
gamest.grid(row=2, column =1)


                



windows.mainloop()
