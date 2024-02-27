# Abdul_Muizz.
# 0321-2266448.
# www.legendgamerz@gmail.com

# Question No. 4:
#Create a program that calculates the sum of the digits of a given number. For example, if the input is 12345, the output should be 15.

#First we define a function which will break down the number which will later be summed.
def sum_of_digits(number):
    sum=0                   #Firse we declare a local variable "sum" and assign it a integer value 0.
    while number>0:         #A while loop is used with a condition.
        digit = number%10   #Here we use modulo to seprate the digits from number.
        sum += digit
        number//=10
    return sum

number=int(input("Enter a number whose sum of digits you want :"))
sum_digit=sum_of_digits(number)
print(f"The sum of the digits of number '{number}' is '{sum_digit}'")