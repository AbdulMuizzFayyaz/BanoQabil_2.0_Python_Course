# Abdul Muizz
# www.legendgamerz@gmail.com

# Question No. 7:
# Write a program that checks if a given number is prime or not. Display an appropriate message.

def is_prime(number):          #Here we define a function that will check if number is prime.
    if number <= 1:            #Check if number is less than 1.             
        return False           #If number is less than 1,return false as those number won't be prime.
    for i in range(2, number): #Using a for loop to get the range of number.
        if number % i == 0:    #Checking the remainder of numbers.
            return False       #If number leaves no remainder then its not a prime number so return false.
    return True                #Otherwise return true ,showing that the number is prime.


try:
    number = int(input("Enter a number: "))                 #Taking user input.
except ValueError:
    print("Invalid input!,Please enter a valid integer.")   #Using error handling.

if is_prime(number):                        #Using condition for our function.
  print(f"{number} is a prime number!")     #If condition is true ,then give an appropiate output.
else:                                       
  print(f"{number} is not a prime number.") #If condition is not true then print that the given number is not prime.
