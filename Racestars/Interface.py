from tkinter import *
import tkinter as tk

import Constructor
import Drivers
driversss = ["Driver", "Team","Points", "Reserve", "Fastest Laps", "Podia", "Wins", "Points Finish"]
constructorsss = ["Team", "Drivers", "Reserve Driver", "Points", "Wins"]
LARGE_FONT= ("Verdana", 12)
entries = {}
fields = ["Name Driver", "Points", "Fastest Laps", "Podia", "Wins", "Points Finish"]


choices = []
for i in range(len(Constructor.Constructor)):
    choices.append(Constructor.Constructor[i]["Name"])


class Racestars(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}

        for F in (homePage, driversPage):

            frame = F(container, self)

            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(homePage)

    def show_frame(self, cont):
        frame = self.frames[cont] 
        frame.tkraise()

class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        controller.title("Racestars")


        self.drivers = LabelFrame(self, text = "Drivers")
        self.constructor = LabelFrame(self, text = "Constructor")
        self.drivers.grid(row = 0, column = 0, sticky = N)
        self.constructor.grid(row = 0, column = 2, sticky = N)

        global driversss
        self.gridMaking(31,len(driversss), 0, "drivers")

        global constructorsss
        self.gridMaking(11,len(constructorsss), len(driversss)+ 2, "constructor")

        
        
        button = tk.Button(self, text= "Edit drivers",
                            command=lambda: controller.show_frame(driversPage))
        button.grid(row=99,column=1)

        quiting = tk.Button(self, text="Exit", command = self.Exit)
        quiting.grid(row = 99, column = 2)

    def gridMaking(self, height, width, offset, option):
        h = 0
        height = int(height)
        width = int(width)
        offset = int(offset)
        for i in range(height):
            for j in range(width):
                if option == "drivers":
                    if i == 0:
                        global driversss
                        w = tk.Label(self.drivers, text=driversss[h])
                    else:
                        
                        w = tk.Label(self.drivers, text="test")
                    w.grid(row=i, column=j+offset)
                    h += 1
                elif option == "constructor":
                    if i == 0:
                        w = tk.Label(self.constructor, text=constructorsss[h])
                    else:
                        w = tk.Label(self.constructor, text="test")
                    w.grid(row=i, column=j+offset)
                    h += 1
                else:
                    print("Not a labelframe.")
                    
     

    def Exit(self): 
        app.destroy()   

        

class driversPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.drivers = LabelFrame(self, text = "Drivers")
        self.drivers.grid(row = 0, column = 0, sticky = N)

        self.editor = LabelFrame(self, text = "New driver")
        self.editor.grid(row=0, column = 2, sticky = N)

        global driversss
        self.gridMaking(10,len(driversss), 0, "drivers")

        global fields
        #self.makeform(fields)
        self.makeform(fields)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(homePage))
        button1.grid(row = 99, column = 1)
        submit = Button(self, text = "Submit driver", command=lambda: print(self.getFormEntry()))
        submit.grid(row=99, column =3)

    def nothing(self):
        pass
        
    def getFormEntry(self):
        entry2 = {}
        global fields
        


        return entry2

    def gridMaking(self, height, width, offset, option):
        h = 0
        height = int(height)
        width = int(width)
        offset = int(offset)
        for i in range(height):
            for j in range(width):
                if option == "drivers":
                    if i == 0:
                        global driversss
                        w = tk.Label(self.drivers, text=driversss[h])
                    else:
                        if j == 0:
                            w = tk.Button(self.drivers, text="edit")

                        else:
                            w = tk.Label(self.drivers, text="test")

                    w.grid(row=i, column=j+offset)
                    h += 1

                elif option == "constructor":
                    if i == 0:
                        w = tk.Label(self.constructor, text=constructorsss[h])
                    else:
                        w = tk.Label(self.constructor, text="test")
                    w.grid(row=i, column=j+offset)
                    h += 1

            
                else:
                    print("Not a labelframe.")


    def makeform(self, fields):
        entrie = {}
        for field in fields:
            row = Frame(self.editor)
            lab = Label(row, width=22, text=field+": ", anchor='w')
            ent = Entry(row)
            ent.insert(0,"")
            row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
            lab.pack(side = LEFT)
            ent.pack(side = RIGHT, expand = YES, fill = X)
            entrie[field] = ent.get()

        team_name = Label(self.editor, text = "Team :")
        team_name.pack(side = LEFT, padx = 5 ,pady = 5)

        teamvar = StringVar(self)
        global choices
        teamvar.set(choices[0])
        team_entry = OptionMenu(self.editor, teamvar, *choices)
        team_entry.pack(side = RIGHT)

        Reserve = IntVar(self)
        isReserve = Checkbutton(self.editor, text = "Reserve", variable=Reserve)
        isReserve.pack(side = RIGHT)

        entrie["Team"] = teamvar.get()
        entrie["Reserve"] = Reserve.get()
        
           
        

app = Racestars()
app.mainloop()
