from tkinter import *
from tkinter import ttk

# def nameGcode():
#     def submit2():
#         fileName2 = str(fileName.get())

#     window4 = Tk()
#     cordGui = Canvas(window4, width=600, height=400)
#     cordGui.grid(columnspan=1, rowspan = 5)
#     instruct1 = Label(window4, text="Please Name the Gcode File/Project")
#     instruct1.grid(column=0, row = 1)
#     instruct1.configure(font = "Corbel 15 bold underline")

#     fileName=StringVar()
#     fileNameEntry = Entry(window4,textvariable = fileName, font=('Corbel',20,'normal'))
#     fileNameEntry.grid(column=0, row = 2)
#     submitButton=Button(window4,text = 'Submit', command = submit2)
#     submitButton.configure(font = "Corbel 11", bg = "#FF0000", fg="white", height =2, width =20)
#     submitButton.grid(column=0, row = 3)


def setPoints(points):
    window3 = Tk()
    numCords = points
    numRows = numCords + 3
    windowHeight = 400
    selectedCords = []
    selectedPolarity = []
    if(numRows*30 >> 400):
        windowHeight = (numRows*30)+30
    cordGui = Canvas(window3, width=600, height=windowHeight)
    cordGui.grid(columnspan=3, rowspan = numRows)

    instruct1 = Label(window3, text="Enter Probe Points")
    instruct1.grid(column=1, row = 0)
    instruct1.configure(font = "Corbel 15 bold underline")
    instruct2 = Label(window3, text="(X Y Z) in mm")
    instruct2.configure(font = "Corbel 11")
    instruct2.grid(column=1, row = 1)

    def writeGcode():
        file=open("file.gcode", "w+")
        for i in range(numCords):
            #writeGcode for magnet servo angle (M280 Sx)
            polarityFinal = selectedPolarity[i].get()
            posAngle = "0"
            negAngle = "180"
            neuAngle = "90"
            if polarityFinal == "Positive":
                file.write("M280 S" + posAngle)
                file.write('\n')
            if polarityFinal == "Negative":
                file.write("M280 S" + negAngle)
                file.write('\n')
            if polarityFinal == "Neutral":
                file.write("M280 S" + neuAngle)
                file.write('\n')
            if polarityFinal == "Select Polarity":
                file.write("M280 S" + neuAngle)
                file.write('\n')

            ##Write Gcode for movement (g1)
            unModdedCords = selectedCords[i].get()
            print(polarityFinal)
            moddedCords = unModdedCords.split(" ")
            x = moddedCords[0]
            y = moddedCords[1]
            z = moddedCords[2]
            gCodeStr = ("G1 X" + x + " Y" + y + " Z" + z)
            file.write(gCodeStr)
            file.write('\n')
            #Write Gcode for hold
            #do x
        window3.destroy()

    for y in range(numCords):
        cordEntry=Entry(window3)
        cordEntry.grid(row=y+2,column=2)
        selectedCords.append(cordEntry)
        instruct3 = Label(window3, text="Enter Coordinates for point " + str(y+1))
        instruct3.configure(font = "Corbel 11")
        instruct3.grid(column=0, row = y+2)

        polarities =ttk.Combobox(values=["Neutral", "Positive", "Negative"]) 
        polarities.set("Select Polarity")
        polarities.grid(column=1, row=y+2)
        selectedPolarity.append(polarities)

    buttonSubmitCords = Button(window3,text="Submit", command=writeGcode)
    buttonSubmitCords.grid(row=numRows-1, column=1)
    window3.mainloop()