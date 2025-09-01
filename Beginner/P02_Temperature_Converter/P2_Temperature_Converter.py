import re
import sys

def celsius_to_fahrenheit(temp_in_celcius):
    return (9.0/5.0)*temp_in_celcius + 32

def celsius_to_kelvin(temp_in_celcius):
    return temp_in_celcius + 273.15

def fahrenheit_to_celsius(temp_in_fahrenheit):
    return (5.0/9.0)*(temp_in_fahrenheit-32)

def fahrenheit_to_kelvin(temp_in_fahrenheit):
    return ((5.0/9.0)*(temp_in_fahrenheit-32))+273.15

def kelvin_to_celcius(temp_in_kelvin):
    return temp_in_kelvin - 273.15

def kelvin_to_fahrenheit(temp_in_kelvin):
    return ((9.0/5.0)*(temp_in_kelvin-273.15)) + 32


user_input=input("Temperature With Unit (C,F or K): ")
match = re.match(r'([0-9]+(?:\.[0-9]+)?)\s*([A-Za-z]+)',user_input)

if match:   
    numercial,unit= match.groups()
    numercial = float(numercial)
    if unit.lower().strip() == 'c':
        print(f"For: {numercial} °{unit.upper()}")
        print(f"In Fahrenheit: {celsius_to_fahrenheit(numercial)}°F") 
        print(f"In Kelvin: {celsius_to_kelvin(numercial)}°K") 

    elif unit.lower().strip() == 'f':
        print(f"For: {numercial} °{unit.upper()}")
        print(f"In Celcius: {fahrenheit_to_celsius(numercial)}°C") 
        print(f"In Kelvin: {fahrenheit_to_kelvin(numercial)}°K") 

    elif unit.lower().strip() == 'k':
        print(f"For: {numercial} °{unit.upper()}")
        print(f"In Celcius: {kelvin_to_celcius(numercial)}°C") 
        print(f"In Fahrenheit: {kelvin_to_fahrenheit(numercial)}°F") 

    else:
        sys.exit("Inappropriate Value Entered")

else:
    sys.exit("Enter a Valid value Try Agiann.....")