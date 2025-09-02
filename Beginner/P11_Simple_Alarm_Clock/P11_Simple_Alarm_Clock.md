# Python Alarm Clock

A simple **command-line Alarm Clock** built in Python.  
Set an alarm for a specific time (and optionally date), and the program will countdown and alert you when the time is reached.

---

## Features
- Set an alarm using **HH:MM** format (24-hour or 12-hour with AM/PM).  
- Option to schedule for the **next day** or multiple days ahead.  
- Option to specify a **custom date** (YYYY-MM-DD).  
- Displays a **live countdown** in hours, minutes, and seconds.  
- Alerts with a message when the alarm time is reached.  
- Handles invalid input gracefully.

---

## Usage Example

```
Time to set alarm for(HH:MM) : 18:30
The time entered has already passed. For next day press 1 or number of days you want to add, or press enter to enter date: 1
Setting alarm for 2025-09-02 06:30 PM
Time left: 23:45:10
```


**After countdown ends:**
```
⏰ ALARM!
```


**Custom Date Example:**
```
Time to set alarm for(HH:MM) : 08:00
The time entered has already passed. Press Enter to enter date:
Enter Date (YYYY-MM-DD): 2025-09-05
Setting alarm for 2025-09-05 08:00 AM
Time left: 72:15:00
```


**Invalid Input Example:**
```
Time to set alarm for(HH:MM) : 25:00
ValueError: Should be in correct format
````

## How It Works

### Input Validation
- Accepts **HH:MM** or **HH:MM AM/PM** formats.
- Checks if the time has already passed today.
- If time passed, allows user to:
  - Schedule for the **next day**
  - Add **multiple days**
  - Enter a **specific date**

### Countdown
- Calculates remaining seconds between now and alarm time.
- Displays a **live countdown** in the format `HH:MM:SS`.
- Uses a `while` loop and `time.sleep(1)` to update countdown every second.

### Alarm Trigger
- When the countdown reaches zero, prints:<br>
`⏰ ALARM!`

## Author
Made with ❤️ by Pratyaksh Yadav