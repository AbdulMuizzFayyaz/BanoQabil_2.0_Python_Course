# Abdul_Muizz.
# www.legendgamerz@gmail.com

# Question No. 1:
# Write a Python program that takes an integer input from the user and checks if it's even or odd. Display an appropriate message.

#Declare a variable with integer datatype.
try:
    number = int(input("Enter a number you want to check if its even or odd :"))

#Now we use if else condition to differentiate even and odd number.

    if number%2 == 0:
        print(f"'{number}' is a even number.")
    else:
        print(f"'{number}' is a odd number.")
except ValueError:                               
    print("Please enter a integer value.")
