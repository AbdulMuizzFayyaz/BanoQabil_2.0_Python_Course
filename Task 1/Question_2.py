# Abdul_Muizz.
# 0321-2266448.
# www.legendgamerz@gmail.com

# Question No. 2:
# Create a program that generates a multiplication table for a given number. Allow the user to input the number and display the table.

#Declare a variable with integer datatype.
try:
    table=int(input("Enter the number whose table you want :"))

#Now we user for loop to print Table.
    for i in range(1,11):
        answer=table*i
        print(f"{table}x{i}={answer}")
except:
    print("Please enter a integer value.")