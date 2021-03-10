counter = 1
while counter <= 5:
    number = int(input('Guess lucky number: '))
    print('Your ', counter, 'guess and Lucky number is: ' , int(number))
    if number == 8 or number == 2:
        print('Good guess!') 
    else:
        print('Try again!')

    if counter == 5:
        print('Game over!')
    counter = counter + 1