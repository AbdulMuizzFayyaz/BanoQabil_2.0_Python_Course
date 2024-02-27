# # Abdul Muizz
# # www.legendgamerz@gmail.com

# #Question No. 5:
# #FizzBuzz Game:
# Implement the FizzBuzz game in Python. Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."

for i in range(1, 101):             #Using a for loop to get numbers from 1-100
  if i % 3 == 0 and i % 5 == 0:     #Using logical operator 'and' to check if number is multiple of both 3 and 5.
    print("FizzBuzz")               #If number is multiple of both 3 and 5 ,prints Fizz Buzz.
  elif i % 3 == 0:                  #Checking if number is multiple of 3.
    print("Fizz")                   #If number is multiple of 3, prints Fizz
  elif i % 5 == 0:                  #Checking if number is multiple of 5.
    print("Buzz")                   #If number is multiple of 5, prints Buzz.
  else:                             #If number don't match any of the conditions above.
    print(i)                        #Then print the number that is not multiple of 3 and 5.
