userEnter = input('Please enter string in ' ' or " " :')
digits = 0
letters = 0
for x in userEnter:
    if x.isalpha():
        letters += 1
    else:
        digits += 1

print('Letters:', letters, 'Digits:', digits)
