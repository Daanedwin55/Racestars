 
import json
import sys
import os

cwd = os.getcwd()

class DriverAPI(object):
        def __init__(self, jsonF):
                self.data = json.load(jsonF)
                self.filename = jsonF
 
        def writeData(self,data):
                with open(self.filename.name,'w') as f:
                        json.dump(data,f,indent=4)
                       
        def getAllTeamsSet(self):
                team = []
                for d in self.data["Drivers"]:
                        team.append(d["team"])
                return set(team)
 
        def getAllDriversSet(self):
                name = []
                for d in self.data["Drivers"]:
                        name.append(d["naam"])
                return set(name)
 
        def getRawData(self):
                return self.data
 
        def getDriverCount(self):
                k = 0
                for d in self.data["Drivers"]:
                     k = k +1
                return int(k)+1
 
        #Driver specific getters
        def getDriverTeam(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["team"]
                       
        def getDriverPoint(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["Points"]
 
        def getDriverPointFinish(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["PointsFinish"]
 
        def getDriverReserveStatus(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["Reserve"]
 
        def getDriverPodia(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["Podia"]
                       
        def getDriverFastestLap(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["FastestLap"]
        def getDriverWin(self, driverName):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                return d["Wins"]
 
        #Driver specific setters
        def setDriverTeam(self, driverName, team):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                d["team"] = team
                       
        def setDriverPoint(self, driverName, points):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                d["Points"] = points
 
        def setDriverPointFinish(self, driverName, pf):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                d["PointsFinish"] = pf
 
        def setDriverReserveStatus(self, driverName, status):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                d["Reserve"] = status
 
        def setDriverPodia(self, driverName, podia):
                for d in self.data["Drivers"]:
                        if self.data["Drivers"][d]["naam"] == driverName:
                                d["Podia"] = podia

        def setDriverFastestLap(self, driverName, fl):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                            d["FastestLap"] = fl
                               
        def setDriverWin(self, driverName, winc):
                for d in self.data["Drivers"]:
                        if d["naam"] == driverName:
                                d["Wins"] = winc
 
        #Adders moeten nog Daddy UwU
        def addDriver(self,naam,fastestLap,podia,wins,pointsFinish, points, team, reserve):
                with open(r'{0}'.format(self.filename.name)) as json_file:
                        data = json.load(json_file)
                       
                        temp_data = data["Drivers"]
                        print(type(temp_data))
                        new_driver = {
                       
                                 "naam":naam,
                                 "team":team,
                                "Points" : points,
                                "Reserve": reserve,
                                "FastestLap": fastestLap,
                                "Podia": podia,
                                "Wins": wins,
                                "PointsFinish": pointsFinish
 
                        }
 
                        temp_data.append(new_driver)
                self.writeData(data)
 
