import tkinter as tk
from tkinter import *
import os

import Constructor
import DriverAPI as DAPI

cwd = os.getcwd()

jsonfile = open(r"{0}/Racestars/Drivers.json".format(cwd), "r", encoding="utf-8")

Data = DAPI.DriverAPI(jsonfile)


class Racestars(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.minsize(600, 400)

        self.frames = {}

        for F in (homePage, driversPage):

            frame = F(container, self)

            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(homePage)

    def show_frame(self, cont):
        frame = self.frames[cont] 
        frame.tkraise()

    def exit(self):
        self.destroy()


class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        controller.title("Racestars")

        self.makeLabfrm()
        self.makeButtons()
        self.driverStanding()
        self.constructorStanding()
        
    def makeLabfrm(self):

        self.drivers = LabelFrame(self, text = "Drivers")
        self.constructor = LabelFrame(self, text = "Constructor")
        self.drivers.grid(row = 0, column = 0, sticky = N)
        self.constructor.grid(row = 0, column = 2, sticky = N)

    def makeButtons(self):

        DriverButton = tk.Button(self, text="Drivers", command=lambda: self.controller.show_frame(driversPage))
        DriverButton.grid(row = 99, column = 1)

        quitButton = tk.Button(self, text="Exit", command= lambda: self.exit())
        quitButton.grid(row = 99, column = 2)

    def driverStanding(self):
        global Data
        countData = Data.getDriverCount()
        allData= Data.getRawData()
        
        driverTitle = ["Driver", "Team","Points", "Reserve", "Fastest Laps", "Podia", "Wins", "Points Finish"]
        h = 0
        test = []
        s = 0

        for i in range(countData+1):
            driverData = allData["Drivers"][i-1]
            for x in driverData.values():
                test.append(x)

            
            for j in range(len(driverTitle)):
                if i == 0:

                    tabel = tk.Label(self.drivers, text = driverTitle[h])

                else:
                    
                    s = s % 8

                    if s == 1:

                        ID = test[1] 
            
                        Con = Constructor.Constructor[ID]["Name"]

                        tabel = tk.Label(self.drivers, text = Con)
                    else:
                        tabel = tk.Label(self.drivers, text = test[s])
                    s += 1
                    if s == 8:
                        del test[:8]
                        

                tabel.grid(row = i, column = j)

                h += 1
        

    def constructorStanding(self):
        constructorTitle = ["Team Name", "Driver #1", "Driver #2", "Reserve rijder", "Points", "Wins"]
        choices = []
        for con in Constructor.Constructor:
            choices.append(Constructor.Constructor[con]["Name"])
        choices.pop(0)
        h = 0

        for i in range(len(choices) + 1):

            for j in range(len(constructorTitle)):
                
                if i == 0:
                    tabel = tk.Label(self.constructor, text = constructorTitle[h])

                else:
                    tabel = tk.Label(self.constructor, text = "test")
            
                tabel.grid(row = i, column = j)

                h += 1


    def exit(self):
        self.controller.exit()


class driversPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # Making the entries
        self.driverEntry = tk.Entry()
        self.pointsEntry = tk.Entry()
        self.fastestLapEntry = tk.Entry()
        self.podiaEntry = tk.Entry()
        self.winsEntry = tk.Entry()
        self.pointsfEntry = tk.Entry()
        self.pointsfinishEntry = tk.Entry()
        self.teamvar = StringVar(self)
        self.Reserve = IntVar(self)


        self.controller = controller
        controller.title("Racestars")

        self.makeLabfrm()
        self.makeButtons()
        self.driverStanding()
        self.makeEditor()
        self.makeEntries()
        
    def makeLabfrm(self):

        self.drivers = LabelFrame(self, text = "Drivers")
        self.driverEditor = LabelFrame(self, text = "Editor")
        self.drivers.grid(row = 0, column = 0, sticky = N)
        self.driverEditor.grid(row = 0, column = 2, sticky = N)

    def makeButtons(self):
        DriverButton = tk.Button(self, text="HomePage", command=lambda: self.controller.show_frame(homePage))
        DriverButton.grid(row = 99, column = 1)

        quitButton = tk.Button(self, text="Exit", command= lambda: self.exit())
        quitButton.grid(row = 99, column = 2)

        submitButton = tk.Button(self.driverEditor, text="Submit", command=lambda: self.getEntry())
        submitButton.grid(row = 99, column = 2)

    def driverStanding(self):
        global Data
        countData = Data.getDriverCount()
        allData= Data.getRawData()
        
        driverTitle = ["Driver", "Team","Points", "Reserve", "Fastest Laps", "Podia", "Wins", "Points Finish"]
        h = 0
        test = []
        s = 0

        for i in range(countData+1):
            driverData = allData["Drivers"][i-1]
            for x in driverData.values():
                test.append(x)

            
            for j in range(len(driverTitle)):
                if i == 0:

                    tabel = tk.Label(self.drivers, text = driverTitle[h])

                else:
                    
                    s = s % 8

                    if s == 1:

                        ID = test[1] 
            
                        Con = Constructor.Constructor[ID]["Name"]

                        tabel = tk.Label(self.drivers, text = Con)
                    else:
                        tabel = tk.Label(self.drivers, text = test[s])
                    s += 1
                    if s == 8:
                        del test[:8]
                        

                tabel.grid(row = i, column = j)

                h += 1
        

    def makeEditor(self):
        editorLabel = tk.Label(self.driverEditor, text = "Driver Editor") 
        editorLabel.grid(row = 0, column = 0, sticky = W)

        driverName = tk.Label(self.driverEditor, text = "Drivers Name")
        driverName.grid(row = 1, column = 1, sticky = W)

        pointsName = tk.Label(self.driverEditor, text = "Points")
        pointsName.grid(row = 2, column = 1, sticky = W) 

        fastestLapName = tk.Label(self.driverEditor, text = "Fastest laps")
        fastestLapName.grid(row = 3, column = 1, sticky = W) 

        podiaName = tk.Label(self.driverEditor, text = "Podia")
        podiaName.grid(row = 4, column = 1, sticky = W)

        winsName = tk.Label(self.driverEditor, text = "Wins")
        winsName.grid(row = 5, column = 1, sticky = W)

        pointsfName = tk.Label(self.driverEditor, text = "Points finishes")
        pointsfName.grid(row = 6, column = 1, sticky = W)

        choices = []
        for i in range(len(Constructor.Constructor)):
            choices.append(Constructor.Constructor[i]["Name"])

        
        self.teamvar.set(choices[0])
        team_entry = OptionMenu(self.driverEditor, self.teamvar, *choices)
        team_entry.grid(row = 7, column = 1, sticky = W)

        
        isReserve = Checkbutton(self.driverEditor, text = "Reserve", variable=self.Reserve)
        isReserve.grid(row = 8, column = 1, sticky = W)




    def makeEntries(self):
        self.driverEntry = tk.Entry(self.driverEditor)
        self.driverEntry.grid(row = 1, column = 3)

        self.pointsEntry = tk.Entry(self.driverEditor)
        self.pointsEntry.grid(row = 2, column = 3)

        self.fastestLapEntry = tk.Entry(self.driverEditor)
        self.fastestLapEntry.grid(row = 3, column = 3)

        self.podiaEntry = tk.Entry(self.driverEditor)
        self.podiaEntry.grid(row = 4, column = 3)

        self.winsEntry = tk.Entry(self.driverEditor)
        self.winsEntry.grid(row = 5, column = 3)

        self.pointsfinishEntry = tk.Entry(self.driverEditor)
        self.pointsfinishEntry.grid(row = 6, column = 3)

    
    def getEntry(self):
        global Data
        newDriver = []
        newDriver.append(self.driverEntry.get())

        newDriver.append(int(self.fastestLapEntry.get()))

        newDriver.append(int(self.podiaEntry.get()))

        newDriver.append(int(self.winsEntry.get()))

        newDriver.append(int(self.pointsfinishEntry.get()))

        newDriver.append(int(self.pointsEntry.get()))

        team = self.teamvar.get()

        for c in Constructor.Constructor:
            if Constructor.Constructor[c]["Name"] == team:
                ID = Constructor.Constructor[c]["Id"]

        newDriver.append(ID)
            

        newDriver.append(self.Reserve.get())

        
        Data.addDriver(newDriver[0], newDriver[1], newDriver[2], newDriver[3], newDriver[4], newDriver[5], newDriver[6], newDriver[7])
        
        self.exit()
        self.controller.show_frame(driversPage)

    def exit(self):
        self.controller.exit()
        
app = Racestars()
app.mainloop()