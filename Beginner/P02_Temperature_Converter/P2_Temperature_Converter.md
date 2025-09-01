# Temperature Converter

A simple **command-line Temprature Converter** built in **Python**.
This calculator can perform conversion from celcius to kelvin ,celcius to farenheit and vice versa.

## Feautures:
- Allows user to input value with unit
- Converts in all three units (°C,°F & °K)
- Ensures correct input format with regex validation
- Prints values in both units excluding the unit entered

## Usage Example:

```
Temperature With Unit (C,F or K): 35C
For: 35.0 °C
In Fahrenheit: 95.0°F
In Kelvin: 308.15°K
```
if you forget to mention the degree at the end the program will end with a message.

```
Inappropriate Value Entered
Enter a Valid value Try Agiann.....
```

### Code Explanation  
Takes a number with unit eg.(**`35C`**) and prints values for both other units (i.e. °F & °K) in current case.
- **`celsius_to_fahrenheit`** → Converts Celsius to Fahrenheit  
  - Formula: **F = (9/5) × C + 32**  

- **`celsius_to_kelvin`** → Converts Celsius to Kelvin  
  - Formula: **K = C + 273.15**  

- **`fahrenheit_to_celsius`** → Converts Fahrenheit to Celsius  
  - Formula: **C = (5/9) × (F − 32)**  

- **`fahrenheit_to_kelvin`** → Converts Fahrenheit to Kelvin  
  - Formula: **K = (5/9) × (F − 32) + 273.15**  

- **`kelvin_to_celsius`** → Converts Kelvin to Celsius  
  - Formula: **C = K − 273.15**  

- **`kelvin_to_fahrenheit`** → Converts Kelvin to Fahrenheit  
  - Formula: **F = (9/5) × (K − 273.15) + 32**

## Author:
Made with ❤️ by Pratyaksh Yadav