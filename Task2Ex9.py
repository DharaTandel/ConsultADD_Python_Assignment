while True:
    number = int(input('Enter your lucky number:'))

    if number == 8:
        print('Correct guess!')
        break
    else:
        answer = input('Do you want to continue? Y/N ')
        if answer == 'N':
            break
        else:
            continue