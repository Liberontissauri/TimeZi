import files
import time
import os

configfilepath = os.getcwd()      #To be implemented
datafilepath = os.getcwd()

colours = {"DEFAULT":"\033[0m",
            "black":"\033[30m",
            "red":"\033[31m",
            "green":"\033[32m",
            "orange":"\033[33m",
            "blue":"\033[34m",
            "purple":"\033[35m",
            "cyan":"\033[36m",
            "light_grey":"\033[37m",
            "dark_grey":"\033[90m",
            "light_red":"\033[91m",
            "light_green":"\033[92m",
            "light_cyan":"\033[96m",
            "light_blue":"\033[94m",
            "yellow":"\033[93m",
            "pink":"\033[95m"}

def addappointment(name,day,hour="allday",colour="DEFAULT"):
    jsoncontent = files.readdata(datafilepath)
 
    jsoncontent["saved_schedules"][day][name]={"name":name,"day": day,"hour":hour,"colour":colour}      #changing json's file's dict contents

    files.savedata(datafilepath, jsoncontent)       #Saving json file

def delappointment(name):
    jsoncontent = files.readdata(datafilepath)      #getting jsonfile contents

    appointment_location = ""

            #Getting the appointment location

    for weekday in jsoncontent["saved_schedules"]:
        for appointment in jsoncontent["saved_schedules"][weekday]:
            if appointment == name:
                appointment_location = weekday      #Storing appointment location

        if appointment_location != "":      #Verifying if the appointment actually exists
            jsoncontent["saved_schedules"][appointment_location].pop(name)      #Deleting appointment

    files.savedata(datafilepath, jsoncontent)       #Saving Changes
    print("[{}] deleted".format(name))

def printappointment(name,weekday):
    jsoncontent = files.readdata(datafilepath)

        #Locating Appointment and printing
    if weekday in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        print("[{}] [{}]{} {}{}".format(jsoncontent["saved_schedules"][weekday][name]["day"],jsoncontent["saved_schedules"][weekday][name]["hour"],colours[jsoncontent["saved_schedules"][weekday][name]["colour"]],name,colours["DEFAULT"]))

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

def nextapp():
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