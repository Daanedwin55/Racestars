# Module which takes car of storage

# Importing Python modules
import json

# Importing self made python scripts
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
        

#writeText(Drivers.driverSetup("Daanedwin", 7, 5, False))
#readText("Data.txt")


def readJson(filename):
    data = []
    with open(filename, "r") as infile:
        for lines in infile:
            data.append(lines)
        return data

def writeJson(data, files):
    if files == "Driver":
        with open("Driver.json", "a") as outfile:
            data = json.dumps(data)
            json.dump(data, outfile, indent=2)
    elif files == "Constructor":
        with open("Constructor.json") as outfile:
            pass

    else:
        print("Invalid file")



writeJson(Drivers.driverSetup("Daanedwin", 7, 5, False), "Driver")
s = (readJson("Driver.json"))
print(s[0])