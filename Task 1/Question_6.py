# # Abdul Muizz
# # www.legendgamerz@gmail.com

# Question No. 7:
# Develop a Python program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards).

text = input("Enter a word or sentence :")

if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome.")