import random
from datetime import date
import tkinter
from datetime import datetime
import time
import threading
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

def updateTime():
    global current_time
    while True:
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%Y:%M:%D")

window = tkinter.Tk()
window.geometry("500x500")

def checkIfPossible():
    selectedDate = [selectedYear.get(),selectedMonth.get(),selectedDay.get()]
    whatMonth = monthList.index(f"{selectedMonth.get()}") + 1
    try:
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        d2 = d1.split('/')
        d0 = date(int(d2[2]),int(d2[1]),int(d2[0]))
        d1 = date(int(selectedYear.get()), whatMonth, int(selectedDay.get()))
        delta = d1 - d0
        howMuchDays = f"that is {str(delta.days)} days away from today."
        if delta.days == 0:
            howMuchDays = "That is today"
        elif delta.days == 69:
            howMuchDays = "OMG ITS 69 DAYS!!!"
        Popup = tkinter.messagebox.showinfo(title="AAAAAAAAAAAAAAAAAAAAAAAAAAA", message=howMuchDays)
    except ValueError:
        randomPosition = random.randint(20,400)
        randomPosition2 = random.randint(20,400)
        DipshitLabel = tkinter.Label(text="Nice Try Dipshit...", font=("Comic_Sans",20))
        DipshitLabel.place(x=randomPosition, y=randomPosition2)
        threading.Timer(3,lambda: DipshitLabel.destroy()).start()

def checkHowMuchDays():
    global selectedDay
    while True:
        try:
            if selectedMonth.get() == "January" or selectedMonth.get() == "March" or selectedMonth.get() == "May" or selectedMonth.get() == "July" or selectedMonth.get() == "August" or selectedMonth.get() == "October" or selectedMonth.get() == "December":
                day.config(values=dayList31)
            elif selectedMonth.get() == "April" or selectedMonth.get() == "June" or selectedMonth.get() == "September" or selectedMonth.get() == "November":
                day.config(values=dayList30)
                if int(selectedDay.get()) > 30:
                    selectedDay.set(30)
            else:
                day.config(values=dayList28)
                if int(selectedDay.get()) > 28:
                    selectedDay.set(28)
        except:
            selectedDay.set(1)

yearList = []
for i in range(6969,0,-1):
    yearList.append(i)
currentDayList = []
dayList30 = []
for i in range (1,31):
    dayList30.append(i)
dayList31 = []
for i in range (1,32):
    dayList31.append(i)
dayList28 = []
for i in range (1,29):
    dayList28.append(i)

monthList = ["January","February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]

selectedYear = tkinter.StringVar()
selectedMonth = tkinter.StringVar()
selectedDay = tkinter.StringVar()
year = ttk.Combobox(window,values=yearList,textvariable=selectedYear)
month = ttk.Combobox(window,values=monthList,state="readonly",textvariable=selectedMonth)
day = ttk.Combobox(window,values=currentDayList,state="readonly",textvariable=selectedDay)
yearLabel = tkinter.Label(text="year")
monthLabel = tkinter.Label(text="Month")
dayLabel = tkinter.Label(text="Day")
yearLabel.place(x=10, y=0)
monthLabel.place(x=180, y=0)
dayLabel.place(x=340, y=0)
year.place(x=10, y=25)
month.place(x=180, y=25)
day.place(x=340, y=25)

threading.Timer(1, checkHowMuchDays).start()

testButton = tkinter.Button(text="Tell date",command=checkIfPossible)
testButton.place(x=200,y= 200)

threading.Timer(1,updateTime).start()
window.mainloop()