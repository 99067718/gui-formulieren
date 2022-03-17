import tkinter
import time
import threading
from tkinter.font import NORMAL
import string
from tkinter import DISABLED, ttk
import random
from tkinter import messagebox
from datetime import datetime
#####################
def CheckIfFilledIn():
    global ConfirmButton
    while True:
        if Email.get() != "" and Name.get() != "":
            ConfirmButton.configure(state=NORMAL)
        else:
            ConfirmButton.configure(state=DISABLED)
#####################
def CheckAnswers():
    try:
        Message = ""
        if int(Age.get()) >= 16 and int(HoursOnRoblox.get()) >= 4:
            Message = "we are glad to let you know that you have been accepted!"
        if int(Age.get()) < 16:
            if int(HoursOnRoblox.get()) < 4:
                Message =  "sadly you have been denied, you must be at least 16 years or older, and"
            else:
                Message = "sadly you have been denied, you must be at least 16 years or older."
        if int(HoursOnRoblox.get()) < 4:
            if Message != "":
                Message = Message + " you also don't have enough monthly hours on roblox."
            else:
                Message = "sadly you have been denied, you must at least play roblox for 4 hours a month"
        SendMail(Email.get(),Name.get(),Message)
    except:
        messagebox.showerror('Oh No', 'Are you sure you filled everything in correctly?')

#####################
import smtplib, ssl
def SendMail(mailAdress, HisName, AcceptOrDenyMessage):
    nameOfSender = random.choice(["Rob", "Lydia", "Jake", "Bob", "Jennifer", "Peter", "David", "Dick"])
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "rbsubmissionsbot@gmail.com"  # Enter your address
    receiver_email = f"{mailAdress}"  # Enter receiver address
    password = "NotMyRealPassword" # enter your password
    message = f"""
    
    Hello {HisName}

    Thanks for your submission to join the \"RB-Battles\"
    We really appreciate your time to enter the forum to enter the RB-Battles, 
    {AcceptOrDenyMessage}
    The first round of RB-Battles begins on 17/06/2022 in the game \"RB-Mayhem\" made by the official Roblox account.

    Yours sincerely {nameOfSender} from RB-Battles,

    Your answers:
    Name: {str(Name.get())}
    Age: {str(Age.get())}
    Username: {str(RobloxAccountName.get())}
    Monthly hours: {str(HoursOnRoblox.get())}

    Your unique registration code: {OriginalCode}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
###############################################
def stringToSeed(seedString): #turns everything into ther ASCII value
    seedList = []
    for x in seedString:
        seedList.append(ord(x))#change every character into its ASCII value
    seedString = ''.join([str(elem) for elem in seedList])#add list together into string
    seed = str(seedString)
    return seed
# Creates seed for your original register code #

Today = datetime.now()
CodeFull = stringToSeed(str(Today))
OriginalCode = CodeFull[len(CodeFull)//2:]
print(OriginalCode)
random.seed(datetime.now())

################################################
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
######################### Smooth close window.
def closeWindow():
    transparency = 1
    for i in range(10):
        time.sleep(0.05)
        transparency -= 0.1
        root.attributes('-alpha',transparency)
    root.destroy()
    exit()
##########################
ageList = []
hourList = []
for i in range(120):
    ageList.append(str(i))
for i in range(744):
    hourList.append(str(i))
root = tkinter.Tk()
root.title("RB-Battles Forum")
root.geometry("500x700")
root.protocol("WM_DELETE_WINDOW", closeWindow)
Title = tkinter.Label(text="Roblox RB-Battles Forum",font=("Comic_Sans",20)).pack()
# Name
FillUrName = tkinter.Label(text="Name").pack()
Name = tkinter.StringVar(value="")
HisName = tkinter.Entry(textvariable=Name).pack()
# Email
EmailText = tkinter.Label(text="Email:").pack()
Email = tkinter.StringVar(value="...@gmail.com")
fillInMail = tkinter.Entry(textvariable=Email).pack()
# First question
question1 = tkinter.Label(text="How old are you?").pack()
Age = tkinter.StringVar(value="...")
Answer1 = ttk.Combobox(values=ageList,textvariable=Age,state="readonly").pack()
question2 = tkinter.Label(text="How many hours do you spend on roblox every month?").pack()
HoursOnRoblox = tkinter.StringVar(value="...")
Answer2 = ttk.Combobox(values=hourList,textvariable=HoursOnRoblox,state="readonly").pack()
RobloxAccountName = tkinter.StringVar(value="...")
Question3 = tkinter.Label(text="Roblox Account name:").pack()
Answer3 = tkinter.Entry(textvariable=RobloxAccountName).pack()
ConfirmButton = tkinter.Button(text="Confirm",state=DISABLED, command= CheckAnswers)
ConfirmButton.pack()
threading.Timer(1.0, CheckIfFilledIn).start()
root.mainloop()