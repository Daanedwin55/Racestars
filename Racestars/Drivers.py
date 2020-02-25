# Here are the drivers proccessed
# Importing needed libraries
import json

# Making a global variable to make drivers with one function

Driver = {
    "Name" : "",
    "Team" : 0,
    "Points" : 0,
    "Reserve": False
}

#   Function to set the Drivers name
def setName(name):
    global Driver
    Driver["Name"] = name

#   Function to set the Drivers team
def setTeam(team):
    global Driver
    Driver["Team"] = team

#   Function to set the points of the Driver
def setPoints(points):
    global Driver
    curPoints = Driver["Points"]
    Driver["Points"] = curPoints + points

#   Function setting if the river is a reserve driver or not
def setReserve(reserve):
    global Driver
    Driver["Reserve"] = reserve

#   Calling all the functions to make a driver
def driverSetup(name, team, points, reserve):
    # Functions can be found further up
    setName(name)
    setTeam(team)
    setPoints(points)
    setReserve(reserve)
    global Driver
    return Driver

def main(function):
    which = function
    
    

#x = driverSetup("Daanedwin", 7, 5, False)


#with open('Data.json', 'a') as outfile:
#    json.dump(x, outfile, indent=4)

