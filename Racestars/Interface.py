from tkinter import *
import tkinter as tk
driversss = ["Driver", "Team","Car","Points", "Reserve", "Fastest Laps", "Podia", "Wins", "Points Finish"]
LARGE_FONT= ("Verdana", 12)

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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(driversPage))
        button.pack()

class driversPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(homePage))
        button1.pack()

# Setting up main frame
#root = Tk()
#Race = Racestars(master=root)
#Race.master.title("Racestars")
#Race.master.minsize(1200, 600)

# Setting up the grid for drivers

#Race.gridMaking(31,9,0, "drivers")

#Race.gridMaking(11,4,10, "constructor")

# Starting the interface

#Race.mainloop()

app = Racestars()
app.mainloop()
