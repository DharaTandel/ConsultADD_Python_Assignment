# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print Consultadd as a string
# If a number is divisible by 5 it should print Python Training as a string
# If a number is divisible by both 3 and 5 it should print Consultadd - Python Training as a string.

a = int(input("Enter a number: "))

if ((a%5 == 0) and (a%3 == 0)):
    print("ConsultADD - Python Training")
elif ((a%3) == 0):
    print("ConsultADD")
elif ((a%5) == 0):
    print("Python Training")
else:
    print("Number is not divided by 3 or 5")