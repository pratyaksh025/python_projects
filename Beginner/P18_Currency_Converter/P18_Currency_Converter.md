# Currency Converter 💱  

This is a simple **Currency Converter** built with Python. The program allows users to convert an amount from one currency to another using fixed exchange rates relative to INR.  

---

## How It Works  
1. The program uses predefined exchange rates relative to the Indian Rupee (INR):  
   ```python
   rates = {
       "INR": 1,
       "USD": 88.05,
       "EUR": 102.37,
       "GBP": 117.64
   }
   ```
2. The user selects:

    - The source currency (e.g., USD)

    - The target currency (e.g., EUR)

    - The amount to convert

3. The program first converts the amount into INR, then into the target currency.

4. Results are displayed with two decimal places.

## Example Usage 

```yml
Available currencies: INR, USD, EUR, GBP
From: USD
To: EUR
Enter amount: 10

10.0 USD = 8.61 EUR
```

## Features

- Supports INR, USD, EUR, GBP.

- Handles invalid currency inputs gracefully.

- Runs in a loop until the user decides to quit.

- Simple and easy-to-use interface.

## How to Run

1. Make sure Python is installed on your system.

2. Save the script as **`P18_Currency_Converter.py`**.

3. Run the file using:

    ```bash
    python currency_converter.py
    ```

## Author
Made with ❤️ by Pratyaksh Yadav




