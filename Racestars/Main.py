import DriverAPI as DAPI
import interfaces
import os


app = interfaces.Racestars()
app.mainloop()


cwd = os.getcwd()

jsonfile = open(r"{0}/Racestars/Drivers.json".format(cwd), "r", encoding="utf-8")
test = DAPI.DriverAPI(jsonfile)

print(test.getAllDriversSet())