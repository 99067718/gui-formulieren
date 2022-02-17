import tkinter
lastColor = "black"
yes = True
window = tkinter.Tk()
for c in range(10):
    for i in range(10):
        if lastColor == "black":
            label1 = tkinter.Label(bg="white",padx=15,pady=10)
            label1.grid(column=c, row=i)
            lastColor = "white"
        else:
            label1 = tkinter.Label(bg="black",padx=15,pady=10)
            label1.grid(column=c, row=i)
            lastColor = "black"
    if yes == True:
        lastColor = "white"
        yes = False
    else:
        yes = True
        lastColor = "black"
window.mainloop()