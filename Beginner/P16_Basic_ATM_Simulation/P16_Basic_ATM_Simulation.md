# ATM Simulation

This is a console-based ATM simulation built in Python. It allows users to create accounts, set or reset PINs, deposit and withdraw money, and check account balances. The simulation maintains a simple in-memory account database.

---

## Features

1. **Account Creation**
   - Users can create a new account by entering:
     - Name (letters only)
     - Account type: Current, Saving, or Zero Balance
     - Initial deposit (must meet minimum balance requirements)
   - The system generates a unique account number for each user.
   - Default PIN for new accounts is `1234`.

2. **Create PIN**
   - Users can set a new 4-digit PIN if their account has the default PIN.

3. **Reset PIN**
   - Users can reset their PIN by providing the current PIN and entering a new one.

4. **Check Balance**
   - Users can check their account balance by entering their account number and PIN.

5. **Deposit Money**
   - Users can deposit money into their account after providing account number and PIN.
   - Only positive amounts are allowed.

6. **Withdraw Money**
   - Users can withdraw money from their account after providing account number and PIN.
   - Withdrawal is allowed only if sufficient balance exists.

---

## Account Structure

Each account is stored as a list:<br>
`[account_number, account_holder_name, account_type, balance, pin]`


- `account_number`: Unique 6-digit integer
- `account_holder_name`: User's name
- `account_type`: Current, Saving, or Zero Balance
- `balance`: Current balance in ₹
- `pin`: 4-digit PIN for authentication

---

## How to Use

1. Run the program:

   ```bash
   python atm_simulation.py
    ```
2. The main menu will display options:
    ```
    Press 1: For Creating Account
    Press 2: To Create Pin
    Press 3: To Reset Pin
    Press 4: To Check Balance
    Press 5: To Deposit Money
    Press 6: To Withdraw Money
    ENTER to close ATM
    Your Choice: 
    ```

3. Follow on-screen prompts to perform actions.

4. Make sure to set your PIN before using deposit, withdrawal, or balance check functions.

## Notes

- Default PIN is 1234. Users must change it for security.

- Account number is automatically generated and guaranteed to be unique.

- Minimum balance requirements:

    - Current and Saving Accounts: ₹500

    - Zero Balance Account: ₹0

- PIN must be exactly 4 digits.

- Deposits and withdrawals must be positive numbers.

- Program handles invalid input gracefully with messages and exceptions.

## Example Flow

**1.** Create a new account<br>
**2.** Set your PIN<br>
**3.** Deposit money<br>
**4.** Check your balance<br>
**5.** Withdraw money<br>

## Author
Made with ❤️ by Pratyaksh Yadav
