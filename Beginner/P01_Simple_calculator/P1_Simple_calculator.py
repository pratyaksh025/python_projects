import sys
#Fucntion definition
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
        

#Taking Input for required parameters:
user_input_for_num1=int(input("Enter number: "))
user_input_for_operator=input("Enter Operator(+,-,/,*): ")

if (user_input_for_num2:=int(input("Enter number: "))) ==0 and user_input_for_operator =='/' :
        sys.exit("Division by Zero Not Allowed")


#Calling function calculate and Printing on Console:    
print("Answer is : ",calculate(user_input_for_num1,user_input_for_operator,user_input_for_num2))