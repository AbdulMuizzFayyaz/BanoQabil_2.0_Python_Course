#Abdul Muizz
#0321-2266448
#www.legendgamerz@gmail.com

#Question:
# Create a Python program that functions as a basic calculator. Your calculator should be able to perform the following operations:
# • Addition
# • Subtraction
# • Multiplication
# • Division

#It is always nice to greet.
print("Welcome to the calculator!")

#Define function for different operations.
#Function for addition.
def Addition():
    try:
        num1=float(input("Enter the first number for the addition :"))
        num2=float(input("Enter the second number for the addition :"))
        sum = num1+num2
        print(f"Addition of {num1} and {num2} is {sum}")
    except:
        print("Invalid Input! Please try again.")    
#Function for subtraction.
def Subtraction():
    try:
        num1=float(input("Enter the first number for the subtraction :"))
        num2=float(input("Enter the second number for the subtraction :"))
        difference = num1-num2
        print(f"Subtraction of {num1} and {num2} is {difference}")
    except:
        print("Invalid Input! Please try again.")
#Function for multiplication.
def Multiplication():
    try:
        num1=float(input("Enter the first number for the multiplication :"))
        num2=float(input("Enter the second number for the multiplication :"))
        Multiplication = num1*num2
        print(f"Multiplication of {num1} and {num2} is {Multiplication}")
    except:
        print("Invalid Input! Please try again.")
#Function for division.
def Division():
    try:
        dividend=float(input("Enter the dividend for division :"))
        divisor=float(input("Enter the divisor for division :"))
        division = dividend/divisor
        print(f"Division of {dividend} with {divisor} is {division}")
    except:
        print("Invalid Input! Please try again.")
#Function for squaring.
def Squaring():
    try:
        base=float(input("Enter the number you want to square:"))
        square=base**2
        print(f"Square of {base} is {square}")
    except:
        print("Invalid Input! Please try again.")
#Function for Square root.
def Square_root():
    try:
        num=float(input("Enter the number, whose square root you want:"))
        root=num**(1/2)
        print(f"Square root of {num} is {root}")
    except:
        print("Invalid Input! Please try again.")
#Function for Inverse.
def Inverse():
    try:
        num=float(input("Enter the number, whose inverse you want:"))
        inverse=num**(-1)
        print(f"Inverse of {num} is {inverse}")  
    except:
        print("Invalid Input! Please try again")
#Function for exponentation.
def Exponentation():
    try:
        base=float(input("Enter the base number:"))
        exponent=float(input("Enter the exponent:"))
        result = pow(base,exponent)
        print(f"{base} raised  to the power {exponent} is equal to {result}")
    except:
        print("Invalid Input! Please try again.")
#Now Implement These Function into main loop for smooth operational calculator.
while True:
    choice = int(input("\n Enter '1' for Addition. \n Enter '2' for Subtraction. \n Enter '3' for Multiplication. \n Enter '4' for Division. \n Enter '5' for Squaring. \n Enter '6' for Square Root. \n Enter '7' for Inverse. \n Enter '8' for Exponentation. \n Enter 'q' to quit"))
    if choice == 1:
        Addition()
    elif choice == 2:
        Subtraction()
    elif choice == 3:
        Multiplication()
    elif choice == 4:
        Division()
    elif choice == 5:
        Squaring()
    elif choice == 6:
        Square_root()
    elif choice == 7:
        Inverse()
    elif choice == 8:
        Exponentation()
    elif choice == 'q':
        break
    else:
        print("Invalid Input!Please try again.")

print("Bye👋")        