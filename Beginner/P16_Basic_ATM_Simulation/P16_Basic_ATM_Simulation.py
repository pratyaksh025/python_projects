               #acc   #holder   #acc type #amt #default pin
account_data=[[123456,"Pratyaksh","Current",5000,1234]]
import random
import re
class atm():
    def __init__(self) -> None:
        self.main()

    def account_number_creation(self):
        account_number= random.randint(111111,999999)
        return account_number
    
    def account_list(self,account_number):
        acc_num_list=[acc for acc,_,_,_,_ in account_data]
        for index, account in enumerate(acc_num_list):
            if account == account_number:
                return index
        else:
            return None

    def create_user(self):
        global account_data
        print("Welcome to registration page")
        
        name = input("Name: ")
        if not name or not re.match(r"^[a-zA-Z ]+$", name):
            print("Invalid name")
            return
        name = name.lower()

        account_type = input("Press 1: For Current\nPress 2: For Saving\nPress 3: For Zero Balance\nYour Choice: ")
        acc_type_map = {"1": "Current", "2": "Saving", "3": "Zero Balance"}
        if account_type not in acc_type_map:
            print("Invalid Choice Made")
            return

        minimum_balance = 500 if account_type in ["1", "2"] else 0
        try:
            amount = float(input(f"Amount (>= {minimum_balance}): "))
            if amount < minimum_balance:
                print("Amount less than minimum required")
                return
        except:
            print("Invalid Input")
            return

        password_default = 1234
        acc_num_list = [acc for acc, _, _, _, _ in account_data]
        account_number = self.account_number_creation()
        while account_number in acc_num_list:
            account_number = self.account_number_creation()

        account_data.append([account_number, name, acc_type_map[account_type], amount, password_default])
        print(f"Account created successfully! Account Number: {account_number}")

                
        

    def create_pin(self,account_number):

        index=self.account_list(account_number)
        if index is not None:
       
            if account_data[index][-1] == 1234:
                try:
                    new_pin= int(input("Enter Pin: "))
                    confirm_pin= int(input("Confirm Pin: "))
                except:
                    raise ValueError("Invalid pin")
            
                if not (1000 <= new_pin <= 9999):
                    print("PIN must be 4 digits")
                    return
                
                if new_pin==confirm_pin:
                    account_data[index][-1]=confirm_pin
                else:
                    print("Pin Doesn't match")
            else: 
                print("Pin Already Set for this user")
        else:
            print("Account Not Found")
    
    def reset_pin(self,account_num,old_pin):
        index=self.account_list(account_num)
        if index is not None:
            if account_data[index][-1] == old_pin:
                try:
                    new_pin= int(input("Enter Pin: "))
                    confirm_pin= int(input("Confirm Pin: "))
                except:
                    raise ValueError("Invalid pin")
            
                if not (1000 <= new_pin <= 9999):
                    print("PIN must be 4 digits")
                    return
                
                if new_pin==confirm_pin:
                    account_data[index][-1]=confirm_pin
                else:
                    print("Pin Doesn't match")
            else:
                print(old_pin," is Incorrect!")
                return None
        else:
            print("Account not found")


    def check_balance(self,account_number,pin):
        index= self.account_list(account_number)
        if index is not None:
            if account_data[index][-1] == 1234:
                self.create_pin(account_data[index][0])

            if account_data[index][-1] == pin:
                print(f"Account: {account_data[index][0]}\nName:{account_data[index][1]}\nBalance: ₹{account_data[index][-2]}/-")
            
            else:
                print("Invalid Pin")
                return
        else:
            print("Account Not Found")

    def deposit(self,account_num,pin):
        index=self.account_list(account_num)
        if index is not None:
            if account_data[index][-1] == 1234:
                self.create_pin(account_data[index][0])

            if account_data[index][-1]==pin:
                print(f"Account: {account_data[index][0]}\nName:{account_data[index][1]}\nCurrent Balance: ₹{account_data[index][-2]}/-")
                print("\n:Amount to deposit in Rupees:")
                try:
                    amount=float(input(""))
                    if amount>0:
                        account_data[index][-2]=account_data[index][-2]+amount
                        print(f"Updated Balance: ₹{account_data[index][-2]}/-")
                    else:
                        print("Value cannot be less than ₹1")
                except:
                    raise ValueError("Invalid Amount")
            
            else:
                print("Invalid Pin")
        else:
            print("Account not found")

    def withdraw(self,account_num,pin):
        index=self.account_list(account_num)
        if index is not None:
            if account_data[index][-1] == 1234:
                self.create_pin(account_data[index][0])

            if account_data[index][-1]==pin:
                print(f"Account: {account_data[index][0]}\nName:{account_data[index][1]}\nCurrent Balance: ₹{account_data[index][-2]}/-")
                print("\n:Amount to withdraw in Rupees:")
                try:
                    amount=float(input(""))
                    if amount>0:
                        if account_data[index][-2]<amount:
                            print(f"Insufficient Balance ₹{account_data[index][-2]}/-")
                        else:
                            account_data[index][-2]=account_data[index][-2]-amount
                            print(f"Withdrawl of ₹{amount} Successful\nRemaining Balance: ₹{account_data[index][-2]}/-")
                    else:
                        print("Value cannot be less than ₹1")
                except:
                    raise ValueError("Invalid Amount")
            else:
                print("Invalid Pin")
        else:
            print("Account not found")

    def main(self):
        print("Welcome To Pratyaksh's ATM Simulation")
        print("Note: for smooth experience start with account creation ")
        while True:
            choice=input("""Press 1: For Creating Account
Press 2: To Create Pin
Press 3: To Reset Pin
Press 4: To Check Balance
Press 5: To Deposit Money
Press 6: To Withdraw Money
ENTER to close ATM
Your Choice: """)
            if choice =="1":
                self.create_user()

            elif choice =="2":
                try:
                    account_number=int(input("Please Enter Account Number: "))
                    self.create_pin(account_number)
                except:
                    raise ValueError("Invalid Input")

            elif choice =="3":
                try:
                    account_number=int(input("Please Enter Account Number: "))
                    pin=int(input("Secure Pin: "))
                    self.reset_pin(account_number,pin)
                except:
                    raise ValueError("Invalid Input")

            elif choice =="4":
                try:
                    account_number=int(input("Please Enter Account Number: "))
                    pin=int(input("Secure Pin: "))
                    self.check_balance(account_number,pin)
                except:
                    raise ValueError("Invalid Input")

            elif choice =="5":
                try:
                    account_number=int(input("Please Enter Account Number: "))
                    pin=int(input("Secure Pin: "))
                    self.deposit(account_number,pin)
                except:
                    raise ValueError("Invalid Input")
            
            elif choice =="6":
                try:
                    account_number=int(input("Please Enter Account Number: "))
                    pin=int(input("Secure Pin: "))
                    self.withdraw(account_number,pin)
                except:
                    raise ValueError("Invalid Input")

            else:
                print("Thank You for Using My Program!")
                break
            

obj=atm()
