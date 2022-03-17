import tkinter
def game():
    import Accountsystem
    import tkinter
    import threading
    from tkinter import ttk
    import random
    import webbrowser
    import time
    question.destroy()
    yourAnswer = []
    numbers = [0,1,2,3,4,5,6,7,8,9]
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1

    def player1CanPressConfirm(*args):

        try:
            string = str(thisIsTheWord.get())
            newstring = Accountsystem.removeCharacters(Accountsystem.removeCharacters(string, numbers))
            if int(len(thisIsTheWord.get())) >= 4 and int(len(thisIsTheWord.get())) <=7:
                continueButton.config(state="active")
            else:
                continueButton.config(state="disabled")
            thisIsTheWord.set(newstring)
        except:
            pass

    def CheckAnswer():
        YourAnswer = []
        wordToAppend = ""
        for i in range(len(answer)):
            match i:
                case 0:
                    wordToAppend = string0.get()
                case 1:
                    wordToAppend = string1.get()
                case 2:
                    wordToAppend = string2.get()
                case 3:
                    wordToAppend = string3.get()
                case 4:
                    wordToAppend = string4.get()
                case 5:
                    wordToAppend = string5.get()
                case 6:
                    wordToAppend = string6.get()
            YourAnswer.append(wordToAppend)
        CheckListValues = "Correct: Wrong:"
        correctLetters = 0
        wrongLetters = 0
        for i in range(len(answer)):
            checkCorrect = ListVersionAnswer[i]
            isItCorrect = YourAnswer[i]
            if isItCorrect == checkCorrect:
                correctLetters += 1
            else:
                wrongLetters += 1
        if wrongLetters == 0:
            global question
            Result.set("Everything is correct!!!")
            windowPlayer2.destroy()
            question = tkinter.Tk()
            congratsLabel = tkinter.Label(text="Congrats, you guessed the word!!!",font=("Comic_Sans", 20)).pack()
            restart = tkinter.Button(text="Press here to play again.", command=game).pack()
            question.mainloop()
        else:
            CheckListValues = f"Correct: {correctLetters} Wrong: {wrongLetters}"
            Result.set(str(CheckListValues))


        

    ####################                  Player 1 Window                        #######################

    def youTried():
        webbrowser.open("https://en.wikipedia.org/wiki/No")
    def exitGame():
        transparency = 1
        for i in range(10):
            time.sleep(0.05)
            transparency -= 0.1
            windowPlayer1.attributes('-alpha',transparency)
        windowPlayer1.destroy()
        exit()
    windowPlayer1 = tkinter.Tk()
    windowPlayer1.protocol("WM_DELETE_WINDOW", youTried)
    windowPlayer1.attributes('-topmost', True)
    windowPlayer1.title("Guess the word (Player 1)")
    windowPlayer1.geometry("300x300")
    text1 = tkinter.Label(text="Enter a word (4 t/m 7 letters):",font=("Comic_Sans",15))
    text1.pack()
    thisIsTheWord = tkinter.StringVar()
    inputBox = tkinter.Entry(textvariable=thisIsTheWord,font=("Comic_Sans",15))
    inputBox.pack()
    continueButton = tkinter.Button(text="Press to continue.", state="disabled",command=lambda:windowPlayer1.destroy())
    continueButton.pack()
    threading.Timer(0, player1CanPressConfirm).start()
    thisIsTheWord.trace("w", player1CanPressConfirm)
    exitButton = tkinter.Button(text="exit",command=lambda: exitGame()).pack()
    windowPlayer1.mainloop()



    ####################                  Player 2 Window                        #######################
    answer = thisIsTheWord.get().upper()
    ListVersionAnswer = Convert(answer)
    YourAnswer = []

    windowPlayer2 = tkinter.Tk() # Creates Window For player 2
    for i in range(len(answer)):
        match i:
            case 0:
                string0 = tkinter.StringVar(value='')
            case 1:
                string1 = tkinter.StringVar(value='') 
            case 2:
                string2 = tkinter.StringVar(value='')
            case 3:
                string3 = tkinter.StringVar(value='')  
            case 4:
                string4 = tkinter.StringVar(value='')
            case 5:
                string5 = tkinter.StringVar(value='')
            case 6:
                string6 = tkinter.StringVar(value='') 
    windowPlayer2.title("Guess the word (Player 2)")
    windowPlayer2.geometry("300x300")
    answerLabel = tkinter.Label(windowPlayer2,text=answer)
    Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    GuessedWord = []

    for i in range(len(answer)):
        exec(f"letter{i} = ttk.Spinbox(windowPlayer2,textvariable=string{i},value=Letters,width=10,font=('sans-serif', 18),state=\"readonly\").pack()")
    ###################### Old Code that didn't work, but had no limits on amount of characters ############################
    #for i in range(len(answer)):
    #   exec(f"global Letter{i}Chosen")
    #   exec(f"Letter{i}Chosen = tkinter.StringVar()")
    #   exec(f"letter{i} = ttk.Spinbox()")
    #   exec(f"letter{i} = ttk.Spinbox(windowPlayer2,textvariable=Letter{i}Chosen,value=Letters,width=10,font=('sans-serif', 18),state=\"readonly\").pack()")
    ########################################################################################################################
    Result = tkinter.StringVar(value="...")
    showResult = tkinter.Label(textvariable=Result).pack()
    Guess = tkinter.Button(text="Guess",command=CheckAnswer)

    Guess.pack()
    windowPlayer2.mainloop()
question = tkinter.Tk()
restart = tkinter.Button(text="Press here to start.", command=game).pack()
question.mainloop()