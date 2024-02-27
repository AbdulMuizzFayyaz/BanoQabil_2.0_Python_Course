# Abdul_Muizz.
# www.legendgamerz@gmail.com

# Question No. 3:
#Write a Python program that calculates the factorial of a given number. Use a loop to perform the calculation.

#Here we define a function to calculate factorial.
def factorial(number):
    if number == 0:     #Making use of condition to check if the number is equal to zero
        return 1        #If number is zero then return 1,as the factorial of 0 is 1.
    else:
        return number*factorial(number-1)                   #If user input a valid integer calculates its factorial.
#Now we declare variable which take user input for factorial.
try:  
    number=int(input("Enter a number for a factorial :"))
except ValueError:
    print("Invalid input!Please enter a valid integer number.")
factorial_value=factorial(number)                           #Store the defined function in a variable and call it.
print(f"The factorial of {number} is {factorial_value}.")   #Print an appropiate statement