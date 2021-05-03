'''
Example file for working with date information
'''
from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is: ", today)

    # print out the date's individual components
    print("Date Components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday | 6=Sunday)
    print("Today's weekday is: ", today.weekday())
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Which is a: ", days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is: ", today)

    # Get the current time
    time = datetime.time(datetime.now())
    print("The current time is: ", time)

    # Get weekday
    today = date.today()
    print(today.weekday())
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    print("Tomorrow will be " + days[(today.weekday()+1)%7])

if __name__ == '__main__':
    main()
