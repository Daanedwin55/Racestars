import DriverAPI as DAPI
import os

cwd = os.getcwd()

jsonfile = open(r"{0}/daddy/Drivers.json".format(cwd), "r", encoding="utf-8")
test = DAPI.DriverAPI(jsonfile)

print(test.getAllDriversSet())