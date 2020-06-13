""" 
    TimeZi is a CLI scheduler app written in python

    usage:
        TimeZi add <name> <weekday> <hour>
        TimeZi delete <name>
        TimeZi next
        TimeZi get <weekday>
        TimeZi today
        TimeZi reset
"""
import Schedule
import files
from docopt import docopt
import os

configfilepath = os.getcwd()      #To be implemented
datafilepath = os.getcwd()

def main():
    arg = docopt(__doc__, version='0.1')

    if arg["add"] == True:
        if arg["<hour>"] != False:
            Schedule.addappointment(arg["<name>"],arg["<weekday>"],arg["<hour>"])
        else:
            Schedule.addappointment(arg["<name>"],arg["<weekday>"])

    if arg["today"] == True:
        Schedule.printtoday()

    if arg["delete"] == True:
        Schedule.delappointment(arg["<name>"])

    if arg["get"] == True:
        Schedule.printday(arg["<weekday>"])

    if arg["next"] == True:
        Schedule.next()

    if arg["reset"] == True:
        files.gendata(datafilepath)

if __name__ == '__main__':
    main()