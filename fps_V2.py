from concurrent.futures import thread
from multiprocessing.connection import wait
import tkinter
import threading
import time
import pygame
from PIL import Image
#old variant: [name,[time],{appDictionary},randint1,randint2,[data with lock += 2 randints],[dataHistory],[data with lock without 2 randints]]
#new variant: [name,[time],{appDictionary},randint1,randint2,[data with lock += 2 randints],[dataHistory],[data with lock without 2 randints]], {achievements}, {collectables}

import pickle
import os
import datetime
import random
import configparser


if os.path.isfile("systemConfig.ini"):#read config if it exists
    config = configparser.ConfigParser()
    config.read('systemConfig.ini')
else:#create config
    with open('systemConfig.ini', 'w') as configfile:
        config = configparser.ConfigParser(allow_no_value=True)
        folder = input('do you have a specific folder where you want to store account data?\nimport the path, or not\n>')
        config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
            'fileExtention' : 'mcld'}
        if os.path.isdir(folder):#check if the inputted folder exists
            if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                folder += '\\'
            config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : 'False', 'AccountName' : 'testaccount'}
        else:
            config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : 'False', 'AccountName' : 'testaccount'}
            try:
                os.mkdir('accounts/')
            except:
                pass
        config.write(configfile)
        print('we created systemConfig.ini, this contains configurations for the account system, change the [User] section at any time')

#load config data
fileExtention = config['DEFAULT']['fileExtention']
path = config['User']['SaveFileFolder']
autoLogin = config['User']['AutoLogin']
autoLoginName = config['User']['AccountName']

def checkSave(pickledData):#check if account is corrupted
    def corruptedAccount():#what to do when account is corrupted
        exit()
    try:
        name, list1, dictionary, num1, num2, data1, data2, data3, achievements, collectables = pickledData
    except:
        name, list1, dictionary, num1, num2, data1, data2, data3 = pickledData
    if data3[1] - data3[0] != data1[1] - data1[0] or data1[0] != data3[0] + (num1 * num2):#check if decryption is possible
        input('Account Data Corrupted, Please find a way to fix it or create a new one')
        corruptedAccount()
        return False
    else:
        print('Account Loaded Correctly')
        return True

def fixData(data):#remove encryption
    data[1] = data[1] - data[0]
    return data

def closeAccount(name, list1, data1):#close the account
    def scrambleData(data,num1,num2,key, num):
        data[0] = key + ((num1 * num2) * num)#add encryption
        data[1] += data[0]
        return data
    global startTime
    closeTime = datetime.datetime.now()#check the time
    list1[0] = round(list1[0] + ((closeTime - startTime).total_seconds()) // 60)#check difference in time from when opened
    num1 = random.randint(0,1000)#key1
    num2 = random.randint(0,1000)#key2
    key = random.randint(0,10000)#masterKey
    #this was used when the data is still encrypted, but if it's decrypted, keep this a comment:
    #data1 = fixData(data1)
    pickle.dump([name, list1, appDataDict, num1, num2, scrambleData(list(data1),num1,num2,key,1), scrambleData(list(data1),num1,num2,key,2), scrambleData(list(data1),num1,num2,key,0), achievements, collectables] , open(f'{path}{name}.{fileExtention}', "wb" ) )

def stringToSeed(seedString): #turns everything into ther ASCII value
    seedList = []
    for x in seedString:
        seedList.append(ord(x))#change every character into its ASCII value
    seedString = ''.join([str(elem) for elem in seedList])#add list together into string
    seed = int(seedString)
    return seed

#for easy loading and testing the account, you can enable this in the config
if autoLogin == 'True':
    search = autoLoginName
else:
    search = input('please give username\n>')


if os.path.exists(f'{path}{search.lower()}.{fileExtention}'):#check if account exists
    print('user found')
    if checkSave(pickle.load( open(f'{path}{search}.{fileExtention}', "rb" ))) == True: #check if it is not corrupted (in my encryption)
        try:
            name, list1, appDataDict, num1, num2, data1, data2, data3, achievements, collectables= pickle.load( open(f'{path}{search.lower()}.{fileExtention}', "rb" )) #load the account
        except:
            name, list1, appDataDict, num1, num2, data1, data2, data3 = pickle.load( open(f'{path}{search.lower()}.{fileExtention}', "rb" )) #load old variant of account
            achievements = {}
            collectables = {}
        startTime = datetime.datetime.now()#start counting how long you are using the program
        data = fixData(data3)#decrypt data
        
else:
    while True:
        print('user not found, do you want to create a new user with this name? Y/N')

        #for easy loading and testing the account
        #answer = 'y'#you can use this to skip the input for testing your code
        answer = input('you will be logged out afterwards\n>')
        if answer.lower() == 'y':
            pickle.dump([search.lower(), [0], {}, 69, 420, [41325, 41325], [41325, 41325], [12345, 12345], {}, {}], open(f'{path}{search.lower()}.{fileExtention}', "wb" ) )
            exit()
        elif answer.lower() == 'n':
            exit()


#use the dictonary for app related files, like for example rebirths or amounts of diamonds
#change this to your app their name
appName = 'FPSGame_Emiel'

if appName not in appDataDict:#if the user hasn't played before
    appDataDict[appName] = [0]
else:
    pass

#this is your game data, for easy use. but you can also just access your gamedata without this
appData = appDataDict[appName]
#it works the same with the collectables and achievements dictionaries as with the account data dict



#close the account correctly (so it won't get corrupted), use this where you need it, and save it here as a comment
#closeAccount(name, list1, data)




#code:


##########################################################################################################################################
highscore = appData[0]
currentScore = 0
listOfMoves = ["Press A", "Press S", "Press D", "Press W", "Triple Click", "Double Click","Click Once", "Press SpaceBar"]
#######################

#########3

        

def restartGame():
    global currentScore
    print("restarting game...")
    threading.Timer(1.0, timerOfGame).start()
    finalScoreLabel.destroy()
    currentScore = 0
    RestartButton.destroy()
    exitButton.destroy()
    movePicker()

def redGradient():
    fadeToRed = ["#003e8a","#103e70","#203d60","#302c50","#402b40","#501a30","#601020","#700010"]
    fadeToBlue = ["#700010","#601020","#501a30","#402b40","#302c50","#203d60","#103e70","#003e8a"]
    for i in range(8):
        color = fadeToRed[i]
        MainFrame.config(bg=color)
        time.sleep(0.2)

    while True:
        if redGradientEnabled == True:
            MainFrame.config(bg="#73000a")
            time.sleep(0.3)
            MainFrame.config(bg="#78000a")
            time.sleep(0.3)
            MainFrame.config(bg="#8a000b")
            time.sleep(0.3)
            MainFrame.config(bg="#96000d")
            time.sleep(0.3)
            MainFrame.config(bg="#8a000b")
            time.sleep(0.3)
            MainFrame.config(bg="#78000a")
            time.sleep(0.3)
        else:
            for i in range(8):
                color = fadeToBlue[i]
                MainFrame.config(bg=color)
                time.sleep(0.2)
            break

def playMusic():
    global redGradientEnabled
    if isMusicEnabled == False:
        pass
    else:
        while True:
            redGradientEnabled = True
            threading.Timer(1.0, redGradient).start()
            pygame.mixer.init()
            pygame.mixer.music.load("Assets/Audio/Phase_Chara.mp3")
            pygame.mixer.music.play()
            time.sleep(219)
            redGradientEnabled = False
            pygame.mixer.music.load("Assets/Audio/Phase1.mp3")
            pygame.mixer.music.play()
            time.sleep(278)

def addScore(event):
    global currentScore
    global highscore
    match chosenMove:
        case "Press A":
            window.unbind("<a>")
        case "Press S":
            window.unbind("<s>")
        case "Press D":
            window.unbind("<d>")
        case "Press W":
            window.unbind("<w>")
        case "Press SpaceBar":
            window.unbind("<space>")
    if chosenMove == "Triple Click" or chosenMove == "Double Click" or chosenMove == "Click Once":
        currentScore += 2
    else:
        currentScore += 1
    if currentScore > highscore:
        highscore = currentScore
        HSValue.set(f"Highscore: {highscore}")
    currentScoreVar.set(f"Current Score: {currentScore}")
    TaskLabel.destroy()
    movePicker()

def exitGame():
    window.destroy()
    exit()

def timerOfGame():
    global finalScoreLabel
    global timeLeft
    global RestartButton
    global exitButton
    timeLeftText = " seconds left"
    timeLeft = inputTime
    timeVar = tkinter.StringVar(value= str(timeLeft) + timeLeftText)
    timerLabel = tkinter.Label(textvariable=timeVar, bg="black",fg="white",font=("Comic Sans MS", 14))
    timerLabel.place(y=10,x=330)
    for i in range(inputTime):
        time.sleep(1)
        timeLeft -= 1
        timeVar.set(str(timeLeft) + timeLeftText)
    if timeLeft <= -1:
            timeVar.set("Nice try Dipshit")
    i = 0
    timerLabel.config(bg="black",fg="red")
    for i in range(10):
        time.sleep(0.05)
        TaskLabel.destroy()
    finalScore = currentScore
    finalTextvar = tkinter.StringVar(value=f"Your final score is: {currentScore}") 
    finalScoreLabel = tkinter.Label(textvariable=finalTextvar, padx=70,pady=50,font=("Comic Sans MS", 14))
    finalScoreLabel.place(x= 100, y= 110)
    RestartButton = tkinter.Button(text="Click here to restart",command= restartGame,padx=10,pady=30)
    RestartButton.place(x= 50, y= 300)
    exitButton = tkinter.Button(text="Close game", command= exitGame,padx=10,pady=30)
    exitButton.place(x= 400, y= 300)


def movePicker():
    global TaskLabel
    global chosenMove
    chosenMove = random.choice(listOfMoves)
    TaskLabel = tkinter.Label(window,text=chosenMove,font=("Comic Sans MS", 12),pady=10,padx=16)
    screen_width = window.winfo_width()
    screen_height = window.winfo_height()
    Xpos = random.randint(0,screen_width -100)
    Ypos = random.randint(50,screen_height-50)
    TaskLabel.place(x=Xpos,y=Ypos)
    match chosenMove:
        case "Press A":
            window.bind("<a>", addScore)
        case "Press S":
            window.bind("<s>", addScore)
        case "Press D":
            window.bind("<d>", addScore)
        case "Press W":
            window.bind("<w>", addScore)
        case "Triple Click":
            TaskLabel.bind("<Triple-Button-1>", addScore)
        case "Double Click":
            TaskLabel.bind("<Double-Button-1>", addScore)
        case "Click Once":
            TaskLabel.bind("<Button-1>", addScore)
        case "Press SpaceBar":
            window.bind("<space>", addScore)

def GetInputTime():
    global inputTime
    global isMusicEnabled
    inputTime = timeThing.get()
    isMusicEnabled = var1.get()
    try:
        inputTime = int(inputTime)
        timerWindow.destroy()
    except ValueError:
        timeThing.set("try entering a number...")

timerWindow = tkinter.Tk()
timerWindow.title("Settings")
showText = tkinter.Label(text="How long do you want to play?")
showText.pack()
timeThing = tkinter.StringVar(value=20)
timerWindow.attributes('-topmost',True)
timerWindow.geometry("200x200")
timerLength = tkinter.Entry(timerWindow,textvariable=timeThing)
timerLength.pack()
confirmButton = tkinter.Button(timerWindow,text="Confirm",command= GetInputTime)
confirmButton.pack()
var1 = tkinter.BooleanVar()
musicEnabled = tkinter.Checkbutton(timerWindow, text="music", variable=var1)
musicEnabled.pack()
timerWindow.mainloop()

window = tkinter.Tk()
threading.Timer(1.0, playMusic).start()
window.attributes('-topmost',True)
window.title("fps")
HSValue = tkinter.StringVar(value=f"Highscore: {highscore}")
window.geometry("500x500")
MainFrame = tkinter.Label(bg="#21354a",padx=1000,pady=1000)
MainFrame.pack()
blackbar = tkinter.Label(padx=1000,pady=12,bg="black")
blackbar.place(x=0,y=0)
highscoreFrame = tkinter.Label(textvariable=HSValue, bg="black",fg="white",font=("Comic Sans MS", 14))
highscoreFrame.place(x= 10, y=10)
currentScoreVar = tkinter.StringVar(value=f"Current Score: {currentScore}")
currentScoreFrame = tkinter.Label(textvariable=currentScoreVar,bg="black",fg="white",font=("Comic Sans MS", 14))
currentScoreFrame.place(y=10,x=150)
threading.Timer(1.0, movePicker).start()
threading.Timer(1.0, timerOfGame).start()
window.mainloop()
appData[0] = highscore

appDataDict[appName] = appData
closeAccount(name, list1, data)