import tkinter as tk
from tkinter import *
from coords import *

window = tk.Tk()
welcomeGui = tk.Canvas(window, width=600, height=400)
welcomeGui.grid(columnspan=3, rowspan = 4)

welcomeText = tk.Label(window, text="Welcome to NRG Probe Control")
welcomeText.configure(font = "Corbel 20 underline bold")
welcomeText.grid(column = 1, row = 1)

def enterMain():
    window.destroy()
    window2 = tk.Tk()
    mainGui = tk.Canvas(window2, width=600, height=400)
    mainGui.grid(columnspan=3, rowspan = 7)
    guide = tk.Label(window2, text="Select Number of Points to Probe")
    guide.configure(font = "Corbel 15 bold")
    guide.grid(column = 1, row = 1)
    numVar = tk.StringVar()

    def submit():
        num = str(numVar.get())
        window2.destroy()
        setPoints(int(num))


    numEntry = tk.Entry(window2,textvariable = numVar, font=('Corbel',20,'normal'))
    numEntry.grid(column=1, row = 2)
    submitButton=tk.Button(window2,text = 'Submit', command = submit)
    submitButton.configure(font = "Corbel 11", bg = "#FF0000", fg="white", height =2, width =20)
    submitButton.grid(column=1, row = 3)

    window2.mainloop()

#---------------------------------
#-------Welcome Menu--------------
#---------------------------------
buttonText = tk.StringVar()
startButton = tk.Button(window, textvariable=buttonText, command=lambda:enterMain())
buttonText.set("Begin")
startButton.configure(font = "Corbel 11", bg = "#FF0000", fg="white", height =2, width =20)
startButton.grid(column=1, row = 2)
window.mainloop()