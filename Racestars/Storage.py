import Drivers

def readText(filename):
    with open(filename, 'r') as f:
         data = f.read()
         print(data)

def writeText(data):
    with open('Data.txt', 'a') as outfile:
        s = ""
        for x,v in data.items():
            s += str(x)
            s += " "
            s += str(v)
            s += ","
        
        outfile.write(s)
        outfile.write("\n")
        

writeText(Drivers.driverSetup("Daanedwin", 7, 5, False))
readText("Data.txt")