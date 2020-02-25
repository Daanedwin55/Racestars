from tkinter import *

class Racestars(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
    
root = Tk()
Race = Racestars(master=root)
Race.master.title("Racestars")
Race.master.minsize(800, 400)
Race.mainloop()
root.destroy()