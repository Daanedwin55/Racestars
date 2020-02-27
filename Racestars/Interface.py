from tkinter import *

import tkinter as tk

class Racestars(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)

    def gridMaking(self, height, width, offset):
        height = int(height)
        width = int(width)
        offset = int(offset)
        for i in range(height):
            for j in range(width):
                w = tk.Label(root, text="Test")
                w.grid(row=i, column=j+offset)

    def emptyGrid(self, height, width, offset):
        height = int(height)
        width = int(width)
        offset = int(offset)
        for i in range(height):
            for j in range(width):
                w = tk.Label(root, text="1111")
                w.grid(row=i, column=j+offset)




root = Tk()
Race = Racestars(master=root)
Race.master.title("Racestars")
Race.master.minsize(800, 400)
Race.gridMaking(31,8,0)
Race.emptyGrid(1,2,8)
Race.gridMaking(11,3,10)

Race.mainloop()
root.destroy()