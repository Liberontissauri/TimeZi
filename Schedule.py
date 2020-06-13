import files
import time
import os

configfilepath = os.getcwd()      #To be implemented
datafilepath = os.getcwd()

def addappointment(name,day,hour="allday"):
    jsoncontent = files.readdata(datafilepath)
 
        #choosing correct place in the json file to store the appointment

    if day not in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        jsoncontent["saved_exceptions"][name]={"name":name,"day": day,"hour":hour}      #changing json's file's dict contents

    else:
        jsoncontent["saved_schedules"][day][name]={"name":name,"day": day,"hour":hour}      #changing json's file's dict contents

    files.savedata(datafilepath, jsoncontent)       #Saving json file

def delappointment(name):
    jsoncontent = files.readdata(datafilepath)      #getting jsonfile contents

    appointment_location = ""

        #Getting the appointment location

    if name in jsoncontent["saved_exceptions"]:
        jsoncontent["saved_exceptions"].pop(name)
        
    else:
        for weekday in jsoncontent["saved_schedules"]:
            for appointment in jsoncontent["saved_schedules"][weekday]:
                if appointment == name:
                    appointment_location = weekday      #Storing appointment location

        if appointment_location != "":
            jsoncontent["saved_schedules"][appointment_location].pop(name)      #Deleting appointment

    files.savedata(datafilepath, jsoncontent)       #Saving Changes
    print("[{}] deleted".format(name))

def printappointment(name,weekday):
    jsoncontent = files.readdata(datafilepath)

        #Locating Appointment and printing

    if weekday == "exception":
        print("[{}] [{}]  {}".format(jsoncontent["saved_exceptions"][name]["day"],jsoncontent["saved_exceptions"][name]["hour"],name))
    if weekday in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        print("[{}] [{}]  {}".format(jsoncontent["saved_schedules"][weekday][name]["day"],jsoncontent["saved_schedules"][weekday][name]["hour"],name))

def gethours(weekday):      #Getting an ordered list of hours of a specific day
    jsoncontent = files.readdata(datafilepath)
    
    unordered_schedule = jsoncontent["saved_schedules"][weekday]        #Storing a copy of the unordered list of appointments

    unordered_hours = []

    ordered_hours = []

    for appointment in unordered_schedule:
        if unordered_schedule[appointment]["hour"] != "allday":
            unordered_hours.append(int(unordered_schedule[appointment]["hour"].replace(":","")))
                #stores the current hour in the ordered hours list as an integer
                #to be able to order the hours
    
    unordered_hours.sort()     #sorts the hours in unordered hours

    for hour in unordered_hours:       #appends each hour in unordered hours to ordered hours in the format: "hours:minutes" (as a string)
        hour = str(hour)
        if len(hour) == 3:
            hour = "0"+ hour
        hour = hour[:2] + ":" + hour[2:]
        ordered_hours.append(hour)

    return ordered_hours

def printday(weekday):
    jsoncontent = files.readdata(datafilepath)

    for hour in gethours(weekday):
        for appointment in jsoncontent["saved_schedules"][weekday]:
            if jsoncontent["saved_schedules"][weekday][appointment]["hour"]==hour:
                printappointment(appointment,weekday)

def printtoday():
    weekday = time.strftime("%A",time.gmtime()).lower()
    printday(weekday)

def next():
    jsoncontent = files.readdata(datafilepath)
    currenthour = int(str(time.strftime("%H",time.localtime())) + str(time.strftime("%M",time.localtime())))
    nexthour = ""

    for hour in gethours(time.strftime("%A",time.gmtime()).lower()):
        if int(hour[:2] + hour[3:]) > currenthour:
            nexthour = hour
            break
    for appointment in jsoncontent["saved_schedules"][time.strftime("%A",time.gmtime()).lower()]:
        if nexthour == jsoncontent["saved_schedules"][time.strftime("%A",time.gmtime()).lower()][appointment]["hour"]:
            printappointment(appointment,time.strftime("%A",time.gmtime()).lower())