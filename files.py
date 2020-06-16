import json
import os

configfilepath = os.getcwd()     #To be implemented
datafilepath = os.getcwd()


def gendata(datafilepath):      #generates the json data file
    content = {'saved_schedules':{
        'monday':{},
        'tuesday':{},
        'wednesday':{},
        'thursday':{},
        'friday':{},
        'saturday':{},
        'sunday':{}
        }
        }

    with open("/".join([datafilepath, "TimeZidata.json"]),"w") as data:         #saving the file
        json.dump(content,data)


if os.path.isfile("/".join([datafilepath, "TimeZidata.json"])) == False:      #Verifying if data file already exists
    gendata(datafilepath)


def readdata(datafilepath):
    with open("/".join([datafilepath, "TimeZidata.json"])) as f:        #reading the data file
        data = json.load(f)

    return data

def savedata(datafilepath,jsonfile):
    with open("/".join([datafilepath, "TimeZidata.json"]),"w") as data:     #saving the data file
        json.dump(jsonfile,data)
