import random
import tkinter
import threading
import time
Amount = 0
CheckBoxAlreadyEnabled = False
lastClicked = ""
def upDown(AddorRemoveNumber = 0):
    global StringNumber
    global Amount
    global lastClicked
    global CheckBoxAlreadyEnabled
    try:
        match AddorRemoveNumber:
            case 1:
                lastClicked = "Up"
            case -1:
                lastClicked = "Down"
    except:
        pass
    Amount += AddorRemoveNumber
    StringNumber.set(Amount)
    if CheckBoxAlreadyEnabled == False:
            CheckBoxAlreadyEnabled = True
            checkBoxButton.configure(state='normal')
    KeepTrackOfAmount(0)
    

def Disco():
    global Amount
    if Amount >69:
        Amount = 69
    for i in range(10):
        window.config(bg="red")
        time.sleep(0.5)
        window.config(bg="green")
        time.sleep(0.5)
        window.config(bg="yellow")
        time.sleep(0.5)
        window.config(bg="blue")
        time.sleep(0.5)

def ChangeColorOnHover(event):
    window.config(bg="yellow")

def DevideOrMultiply(event):
    global Amount
    global checkBoxButton
    global CheckBoxAlreadyEnabled
    match lastClicked:
        case "Up":
            Amount = Amount * 3
            StringNumber.set(Amount)
        case "Down":
            Amount = Amount // 3
            StringNumber.set(Amount)

def Autoclicker():
    global Amount
    while True:
        time.sleep(0.2)
        isEnabled = AutoEnabled.get()
        if isEnabled == True:
            if lastClicked == "Up":
                Amount += 1
            elif lastClicked == "Down":
                Amount -= 1
            else:
                print("An Error Occurred")
            StringNumber.set(Amount)

def KeepTrackOfAmount(event):
    global Amount

    if Amount >= 1:
        window.config(bg="green")
    elif Amount <= -1:
        window.config(bg="red")
    elif Amount == 0:
        window.config(bg="grey")
    elif Amount == 69: 
        downButton.config(state=tkinter.DISABLED)
        UpButton.config(state=tkinter.DISABLED)
        Disco()


window = tkinter.Tk()
window.geometry("500x300")
UpButton = tkinter.Button(text="+1",padx=100,pady=20,command=lambda: upDown(1))
UpButton.pack()
StringNumber = tkinter.StringVar(window,value=Amount)
score = tkinter.Label(textvariable=StringNumber,pady=20,padx=100)
score.bind("<Enter>", ChangeColorOnHover)
score.bind("<Leave>", KeepTrackOfAmount)
score.bind('<Double-Button-1>', DevideOrMultiply)
window.bind("<=>", lambda event: upDown(1))
window.bind("<Up>", lambda event: upDown(1))
window.bind("-", lambda event: upDown(-1))
window.bind("<Down>", lambda event: upDown(-1))
window.bind("<space>", DevideOrMultiply)
score.pack()
AutoEnabled = tkinter.BooleanVar()
checkBoxButton = tkinter.Checkbutton(variable=AutoEnabled,text="AutoClicker",state=tkinter.DISABLED)
checkBoxButton.place(x=0, y=30)
downButton = tkinter.Button(text="-1",padx=100,pady=20,command=lambda: upDown(-1))
downButton.pack()
threading.Timer(1, Autoclicker).start()
window.mainloop()