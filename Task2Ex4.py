#-------4. Break and Continue Game-----------
print("Enter Positive Number to play and Negative Number for End game ")

while True:
    userEnter = int(input("Enter your Number: "))
    if (userEnter > 0):
        print("Good Going!")
        continue
    elif (userEnter < 0):
        print("It's Over!")
        break
    else:
        print("Your Number is: ", userEnter)