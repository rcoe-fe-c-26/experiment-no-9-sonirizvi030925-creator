# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
num = int(input("Enter Number: "))
fact = 1
if num >= 0:
    for i in range(1,num + 1):
        fact = fact * i
    print(f"Factorial of {num} is {fact}") 
else:
     print(f"Factorial of {num} is Not Defined")

