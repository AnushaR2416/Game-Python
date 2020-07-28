import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("135x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

Tops = Frame(root,bg='Cadet Blue', pady=2,width=1350,height=100, relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle = Label(Tops,font=('arial', 50, 'bold'), text="Tic Tac Toe", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root,bg='Powder Blue', bd=10,width=1350,height=600, relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=10, padx=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

bottons = StringVar()
click = True

def checker(bottons):
    global click
    if bottons["text"] == " " and click == True:
        bottons["text"] = "X"
        click=False
        scorekeeper()
    elif bottons["text"] == " " and click == False:
        bottons["text"] = "O"
        click=True
        scorekeeper()

def scorekeeper():
    #check for the X
    if(botton1['text'] == "X" and botton2['text'] == "X" and botton3['text'] == "X"):
        botton1.configure(background="Green")
        botton2.configure(background="Green")
        botton3.configure(background="Green")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," You have just won a game")

    if (botton4['text'] == "X" and botton5['text'] == "X" and botton6['text'] == "X"):
        botton4.configure(background="Green")
        botton5.configure(background="Green")
        botton6.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton7['text'] == "X" and botton8['text'] == "X" and botton9['text'] == "X"):
        botton7.configure(background="Green")
        botton8.configure(background="Green")
        botton9.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton3['text'] == "X" and botton5['text'] == "X" and botton7['text'] == "X"):
        botton3.configure(background="Green")
        botton5.configure(background="Green")
        botton7.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton1['text'] == "X" and botton5['text'] == "X" and botton9['text'] == "X"):
        botton1.configure(background="Green")
        botton5.configure(background="Green")
        botton9.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton1['text'] == "X" and botton4['text'] == "X" and botton7['text'] == "X"):
        botton1.configure(background="Green")
        botton4.configure(background="Green")
        botton7.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton2['text'] == "X" and botton5['text'] == "X" and botton8['text'] == "X"):
        botton2.configure(background="Green")
        botton5.configure(background="Green")
        botton8.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")

    if (botton3['text'] == "X" and botton6['text'] == "X" and botton9['text'] == "X"):
        botton3.configure(background="Green")
        botton6.configure(background="Green")
        botton9.configure(background="Green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", " You have just won a game")


    #Check for O
    if (botton1['text'] == "O" and botton2['text'] == "O" and botton3['text'] == "O"):
        botton1.configure(background="Blue")
        botton2.configure(background="Blue")
        botton3.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton4['text'] == "O" and botton5['text'] == "O" and botton6['text'] == "O"):
        botton4.configure(background="Blue")
        botton5.configure(background="Blue")
        botton6.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton7['text'] == "O" and botton8['text'] == "O" and botton9['text'] == "O"):
        botton7.configure(background="Blue")
        botton8.configure(background="Blue")
        botton9.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton3['text'] == "O" and botton5['text'] == "O" and botton7['text'] == "O"):
        botton3.configure(background="Blue")
        botton5.configure(background="Blue")
        botton7.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton1['text'] == "O" and botton5['text'] == "O" and botton9['text'] == "O"):
        botton1.configure(background="Blue")
        botton5.configure(background="Blue")
        botton9.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton1['text'] == "O" and botton4['text'] == "O" and botton7['text'] == "O"):
        botton1.configure(background="Blue")
        botton4.configure(background="Blue")
        botton7.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton2['text'] == "O" and botton5['text'] == "O" and botton8['text'] == "O"):
        botton2.configure(background="Blue")
        botton5.configure(background="Blue")
        botton8.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")

    if (botton3['text'] == "O" and botton6['text'] == "O" and botton9['text'] == "O"):
        botton3.configure(background="Blue")
        botton6.configure(background="Blue")
        botton9.configure(background="Blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", " You have just won a game")


def reset():
    botton1['text'] = " "
    botton2['text'] = " "
    botton3['text'] = " "
    botton4['text'] = " "
    botton5['text'] = " "
    botton6['text'] = " "
    botton7['text'] = " "
    botton8['text'] = " "
    botton9['text'] = " "

    botton1.configure(background="gainsboro")
    botton2.configure(background="gainsboro")
    botton3.configure(background="gainsboro")
    botton4.configure(background="gainsboro")
    botton5.configure(background="gainsboro")
    botton6.configure(background="gainsboro")
    botton7.configure(background="gainsboro")
    botton8.configure(background="gainsboro")
    botton9.configure(background="gainsboro")

def NewGame():
    n1 = float(PlayerX.get())
    n2 = float(PlayerO.get())
    if (n1 > n2):
        tkinter.messagebox.showinfo("Winner X", " You have just won the match")
    elif (n1 < n2):
        tkinter.messagebox.showinfo("Winner Y", " You have just won the match")
    else:
        tkinter.messagebox.showinfo("Winner X and Y", " The match is Tie")
    reset()
    PlayerX.set(0)
    PlayerO.set(0)



lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X :", padx=2, pady=2, bg='Cadet Blue')
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX= Entry(RightFrame1, font=('arial', 40, 'bold'),bd=2,fg="black", textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player O :", padx=2, pady=2, bg='Cadet Blue')
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO= Entry(RightFrame1, font=('arial', 40, 'bold'),bd=2,fg="black", textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)

btnReset = Button(RightFrame2, text="Reset", font=('arial',40,'bold'), height=1, width=20, command=reset)
btnReset.grid(row=0, column=0,padx=6, pady=11)

btnNewGame = Button(RightFrame2, text="New Game", font=('arial',40,'bold'), height=1, width=20, command=NewGame)
btnNewGame.grid(row=1, column=0,padx=6, pady=11)



botton1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton1))
botton1.grid(row=1, column=0, sticky=S+N+E+W)

botton2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton2))
botton2.grid(row=1, column=1, sticky=S+N+E+W)

botton3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton3))
botton3.grid(row=1, column=2, sticky=S+N+E+W)

botton4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton4))
botton4.grid(row=2, column=0, sticky=S+N+E+W)

botton5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton5))
botton5.grid(row=2, column=1, sticky=S+N+E+W)

botton6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton6))
botton6.grid(row=2, column=2, sticky=S+N+E+W)

botton7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton7))
botton7.grid(row=3, column=0, sticky=S+N+E+W)

botton8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton8))
botton8.grid(row=3, column=1, sticky=S+N+E+W)

botton9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda :checker(botton9))
botton9.grid(row=3, column=2, sticky=S+N+E+W)


root.mainloop()
