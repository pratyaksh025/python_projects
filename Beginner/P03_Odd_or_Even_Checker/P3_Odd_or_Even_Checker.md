# Odd or Even

A simple **command-line Odd Or Even checking  program** built in **Python**.


## Features
- Takes user input. 
- Ensures correct input format with regex validation.

## Usage Example

```
Enter A number to check: 5
5 is an Odd Number

```

If user tries to input anything except number:
```
Enter A number to check: a
Not A Valid Input: a
```

## Code Explaination

**Function `odd_or_even` :**
- returns ``True`` if number is Even.
- returns ``False`` if number is Odd.

```python
def odd_or_even(number):
    if number % 2 == 0:
        return True
    
    return False

```
## Author:
Made with ❤️ by Pratyaksh Yadav
 