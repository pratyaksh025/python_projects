# Simple Calculator

A simple **command-line calculator** built in **Python**.
This calculator can perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features:
- Adds two numbers
- Subtracts two numbers
- Multiplies two numbers
- Divides two numbers (with ZeroDivssion error handling)

## Usage Example:

```
Enter number: 10
Enter Operator: +
Enter number: 5

Answer is : 15

```

if you try to divide a number by **`0`** program will return:

```
Division by Zero Not Allowed
```

## Code Explaination:

**Function `calculate(num1,operator,num2)`:**
- Takes two numbers and an operator
- Returns the result based on the operator

```python
def calculate(num1,operator,num2):
    '''Calculator for two Numbers'''

    if operator =="+":
        return num1+num2
    
    elif operator == "-":
        return num1-num2
    
    elif operator == "*":
        return num1*num2
    
    else:
        return num1/num2
```

## Author:
Made with ❤️ by Pratyaksh Yadav