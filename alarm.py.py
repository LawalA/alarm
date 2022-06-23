import datetime
from signal import alarm
alarmHour = int(input("Hour"))
alarmMinute =int(input("Minute"))
 amPm =str(input("am or pm"))


 if (amPm=="pm"):
     alarmHour =alarmHour +12
while (1==1):
    if(alarmHour == datetime.datetime.now().hour and
    alarmMinute ==datetime.datetime.now().minute):
        print("is time to get up")
        break