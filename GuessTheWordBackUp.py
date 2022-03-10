import tkinter
import threading
from tkinter import ttk
import random
yourAnswer = []

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def player1CanPressConfirm():
    while True:
        try:
            if int(len(thisIsTheWord.get())) >= 4 and int(len(thisIsTheWord.get())) <=7:
                continueButton.config(state="active")
            else:
                continueButton.config(state="disabled")
        except:
            break

def CheckAnswer():
    print(GuessedWord)
    YourAnswer = []
    wordToAppend = ""
    for i in range(len(answer)):
        exec(f"wordToAppend = string{i}.get()")
        YourAnswer.append(wordToAppend)
        
    print(YourAnswer)


def startPlayer2():
    global answer
    global YourAnswer
    global ListVersionAnswer
    global GuessedWord
    answer = thisIsTheWord.get().upper()
    ListVersionAnswer = Convert(answer)
    YourAnswer = []
    windowPlayer1.destroy()
    windowPlayer2 = tkinter.Tk()
    windowPlayer2.title("Guess the word (Player 2)")
    windowPlayer2.geometry("300x300")
    answerLabel = tkinter.Label(windowPlayer2,text=answer)
    Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    GuessedWord = []
    
    for i in range(len(answer)):
        exec(f"global chosenLetter{i}")
        exec(f"global string{i}")
        exec(f"chosenLetter{i} = string{i}")
        exec(f"letter{i} = ttk.Spinbox(windowPlayer2,textvariable=string{i},value=Letters,width=10,font=('sans-serif', 18),state=\"readonly\").pack()")
    ###################### Old Code that didn't work, but had no limits on amount of characters ############################
    #for i in range(len(answer)):
    #   exec(f"global Letter{i}Chosen")
    #   exec(f"Letter{i}Chosen = tkinter.StringVar()")
    #   exec(f"letter{i} = ttk.Spinbox()")
    #   exec(f"letter{i} = ttk.Spinbox(windowPlayer2,textvariable=Letter{i}Chosen,value=Letters,width=10,font=('sans-serif', 18),state=\"readonly\").pack()")
    ########################################################################################################################
    
    Guess = tkinter.Button(text="Guess",command=CheckAnswer)

    Guess.pack()
    windowPlayer2.mainloop()


windowPlayer1 = tkinter.Tk()
for i in range(8):
    exec(f"chosenLetter{i} = 'empty'")
    exec(f"string{i} = tkinter.StringVar(value='')")
windowPlayer1.title("Guess the word (Player 1)")
windowPlayer1.geometry("300x300")
text1 = tkinter.Label(text="Enter a word (4 t/m 7 letters):",font=("Comic_Sans",15))
text1.pack()
thisIsTheWord = tkinter.StringVar()
inputBox = tkinter.Entry(textvariable=thisIsTheWord,font=("Comic_Sans",15))
inputBox.pack()
continueButton = tkinter.Button(text="Press to continue.", state="disabled",command=startPlayer2)
continueButton.pack()
threading.Timer(0, player1CanPressConfirm).start()
windowPlayer1.mainloop()