#Code is my work but learned from freeCodeCamp.org
from tkinter import *

window = Tk() # Creates a Window
window.title("My First GUI") # Name of the Window

def aclick():
    Textinclick = Label(window,text = "Yup I clicked")
    Textinclick.grid(row=3,column=0)

#Now I will create text in the window
Textin = Label(window, text = "Hello World")
Textin2 = Label(window, text= "My name is Poula")

#Creating a Button
Buttonin= Button(window,text = "Click Me",state = DISABLED, padx =50,pady=50, command=aclick,fg='blue',bg='red')#wE CAN ENABLE OR DISABLE. Padx and pady, make it bigger. Notice here how I didnt put () afre aclick
# We can do Hex Color Code
# We can do Textin2 = Label(window, text= "My name is Poula").grid(row=0,column=0)

# Now I need to add it

#Textin.pack()
#Textin2.pack()
#Buttonin.pack()

# We can use pack or grid but not both
#Instead of Packing, I can Grid. Doesnt automatically resize

Textin.grid(row=0,column=0)
Textin2.grid(row=1, column=0) #If there is nothing written, then it wont matter if u put in coloumn 5 or 99
Buttonin.grid(row=2, column=0)


# Now I need program always running
window.mainloop()
    
