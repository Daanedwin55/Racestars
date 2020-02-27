
        # Making of LabelFrames
        self.drivers = LabelFrame(root, text = "Drivers")
        self.constructor = LabelFrame(root, text = "Constructor")
        self.drivers.grid(row = 0, column = 0, sticky = N)
        self.constructor.grid(row = 0, column = 2, sticky = N)
    
        # Making of buttons

        switching = tk.Button(root, text="Switch", command = self.switch)
        switching.grid(row = 99, column = 3)
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