import datetime
import re


date_re = re.compile(r"^\d{4}([-\/])(0[1-9]|1[0-2])\1(0[1-9]|[12][0-9]|3[01])$")

def validate_date(date_str):
    match = date_re.match(date_str)
    if not match:
        return False
    
    sep = match.group(1) 
    try:
        datetime.datetime.strptime(date_str, f"%Y{sep}%m{sep}%d")
        return True
    except ValueError:
        return False
    

def day_of_week(date_str):
    year, month, day = date_str.replace("/", "-").split("-")

    date=datetime.datetime(int(year),int(month),int(day))

    name= date.strftime("%A")
    short= date.strftime(r"%a")
    return name,short


user_date= input("Enter Date(yyyy/mm/dd or yyyy-mm-dd): ")

validation= validate_date(user_date)

if validation:
    full,short=day_of_week(user_date)
    print("Day: ",full)
    print("Short: ",short)

else:
    print("Invalid date")

