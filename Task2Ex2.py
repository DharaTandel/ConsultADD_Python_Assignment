print("Choose following option first: \n Enter 1 - Addition, \n Enter 2 - Substraction, \n Enter 3 - Multiplication, \n Enter 4- Division, \n Enter 5 - Average")
userEnter = int (input("Enter your selection: "))
if ((userEnter == 1) or (userEnter == 2) or (userEnter == 3) or (userEnter == 4)):
    number1 = float(input("Enter the Number1: ")) 
    number2 = float(input("Enter the Number2: "))
    if userEnter == 1:
        answer = number1 + number2
    elif userEnter == 2:
        answer = number1 - number2
    elif userEnter == 3:
        answer = number1 * number2
    elif userEnter == 4:
        answer = number1 / number2
elif userEnter == 5:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    answer = (first + second)/2
else:
    print(userEnter)

if answer < 0:
    print("Answer is NEGATIVE.", answer)
else:
    print("Answer is: ", answer)