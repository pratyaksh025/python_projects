import time
from datetime import datetime, timedelta

alarm_time = input("Time to set alarm for(HH:MM) : ")
alarm_time = alarm_time.strip().upper()

t = None
for tmz in ("%H:%M", "%I:%M %p"):
    try:
        t = datetime.strptime(alarm_time, tmz).time()
        break
    except ValueError:
        pass

if t is None:
    raise ValueError("Should be in correct format")

else:
    alarm_dt = datetime.combine(datetime.now().date(), t)
    if alarm_dt <= datetime.now():
        user = input("The time entered has already passed. For next day press 1 or number of days you want to add, or press enter to enter date: ")
        if user.isdigit() or user == "": 
            if user == "":
                try:
                    date_entered = input("Enter Date (YYYY-MM-DD): ")
                    date_entered = datetime.strptime(date_entered, "%Y-%m-%d").date()
                    new_alarm_dt = datetime.combine(date_entered, t)
                    print(f"Setting alarm for {new_alarm_dt.strftime('%Y-%m-%d %I:%M %p')}")
                    remaining = (new_alarm_dt - datetime.now()).total_seconds()

                    # Countdown
                    while remaining > 0:
                        print(f"\rTime left: {int(remaining)//3600:02}:{(int(remaining)%3600)//60:02}:{int(remaining)%60:02}", end="")
                        time.sleep(1)
                        remaining -= 1
                    
                    print("\n⏰ ALARM! ")
                
                except ValueError:
                    raise ValueError("Date format should be YYYY-MM-DD (08 not supported)")
            else:
                alarm_dt += timedelta(days=int(user))
                print(f"Setting alarm for {alarm_dt.strftime('%Y-%m-%d %I:%M %p')}")
                remaining = (alarm_dt - datetime.now()).total_seconds()

                # Countdown
                while remaining > 0:
                    print(f"\rTime left: {int(remaining)//3600:02}:{(int(remaining)%3600)//60:02}:{int(remaining)%60:02}", end="")
                    time.sleep(1)
                    remaining -= 1

                print("\n⏰ ALARM! ")
        else:
            print("Invalid Input")
    else:
        print(f"Setting alarm for {t}")
        remaining = (alarm_dt - datetime.now()).total_seconds()

        # Countdown
        while remaining > 0:
            print(f"\rTime left: {int(remaining)//3600:02}:{(int(remaining)%3600)//60:02}:{int(remaining)%60:02}", end="")
            time.sleep(1)
            remaining -= 1

        print("\n⏰ ALARM! ")
