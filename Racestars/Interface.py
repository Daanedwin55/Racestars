from tkinter import *
import tkinter as tk
driversss = ["Driver", "Team","Points", "Reserve", "Fastest Laps", "Podia", "Wins", "Points Finish"]

class Racestars(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.drivers = LabelFrame(root, text = "Drivers")
        self.constructor = LabelFrame(root, text = "Constructor")
        self.drivers.grid(row = 0, column = 0, sticky = N)
        self.constructor.grid(row = 0, column = 2, sticky = N)
    
        # Making of buttons

        quiting = tk.Button(root, text="Exit", command = self.Exit)
        quiting.grid(row = 99, column = 1)

    def Exit(self): 
        root.destroy()

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
                    w = tk.Label(self.constructor, text="Test")
                    w.grid(row=i, column=j+offset)
                else:
                    print("Not a labelframe.")


# Setting up main frame
root = Tk()
Race = Racestars(master=root)
Race.master.title("Racestars")
Race.master.minsize(800, 400)

# Setting up the grid for drivers

Race.gridMaking(31,8,0, "drivers")

Race.gridMaking(11,4,10, "constructor")

# Starting the interface

Race.mainloop()
root.destroy()