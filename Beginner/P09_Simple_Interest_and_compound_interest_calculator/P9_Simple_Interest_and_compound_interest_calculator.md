# Simple & Compound Interest Calculator

A **Python command-line calculator** to compute **Simple Interest (SI)**, **Compound Interest (CI)**, and related financial values like Principal, Rate, Time, and Total Amount.

---

## Features
- Calculate **Compound Interest (CI)**.  
- Calculate **Simple Interest (SI)**.  
- Calculate **Amount** based on CI or SI.  
- Calculate **Principal**, **Rate**, or **Time** if other values are known.  
- Handles invalid input gracefully and prompts the user again.  
- Easy-to-use menu-driven interface.

---

## Usage Example

```
This is CI and SI Calculator

CI or 1 To Calculate Compound Interest
SI or 2 to Calculate Simple Interest
A or 3 to Calculate Amount
P or 4 to Calculate Principal
R or 5 to Calculate Rate
T or 6 to Calculate Time
Press Enter to Exit:

Enter Choice: 1
Enter Principal: 1000
Enter Rate: 5
Enter Time: 2
Compound Interest: 102.5

#or

Enter Choice: 2
Enter Principal: 1000
Enter Rate: 5
Enter Time: 2
Simple Interest: 100.0

#or

Enter Choice: 3
1 for CI
2 for SI
Enter Choice: 1
Enter Principal: 1000
Enter Rate: 5
Enter Time: 2
Amount (CI): 1102.5

```

**Invalid Input Example:**
```
Enter Principal: abc
could not convert string to float: 'abc'
```

## How It Works

### `compound_interest(principal, rate, time)`
- Calculates compound interest using the formula.<br>
**CI = P * (1 + R/100)^T - P**
- `P` = Principal  
- `R` = Rate  
- `T` = Time  

Returns the **compound interest**.

### `simple_interest(principal, rate, time)`
Calculates simple interest using the formula:<br>
**SI = (P * R * T) / 100**

Returns the **simple interest**.

### `amount(value, principal, rate, time)`
Calculates total amount based on CI or SI.

### `principal(value, rate, time, amount, interest)`
Calculates Principal if other values are known.

### `rate(value, principal, time, amount, interest)`
Calculates Rate from the given inputs.

### `time(value, principal, rate, amount, interest)`
Calculates Time from the given inputs.

---

## Menu Options
- **1 / CI** → Calculate Compound Interest  
- **2 / SI** → Calculate Simple Interest  
- **3 / A** → Calculate Amount (CI or SI)  
- **4 / P** → Calculate Principal (CI or SI)  
- **5 / R** → Calculate Rate (CI or SI)  
- **6 / T** → Calculate Time (CI or SI)  
- **Press Enter** → Exit the program  

---

## Author
Made with ❤️ by Pratyaksh Yadav



