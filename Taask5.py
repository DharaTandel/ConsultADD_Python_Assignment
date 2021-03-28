#1.

try:
    print('Hello World!')
except SyntaxError:
    print('SyntaxError')


# 2.
from sys import argv
fileName = argv
print('Name of the file entered:',fileName)

while True:   
    try:
        i = open(fileName,'r')
        print("File ready to read!")
        i.close()
    except:
        again = input('Retry? Y/N: ')
        if again == 'Y':
            fileName = input('Enter valid Filename: ')
        else:
            break

# 3.

pwd = int(input('Enter four digits Password: '))
try:
    if (len(str(pwd))>4) or (len(str(pwd))<4):
        raise Exception('The length is too short/long!!! Please provide only four digits')
    else:
        print('SUCCESSFULL!!')
except Exception as err:
    print(err)

# 4.

print('User will only get 3 tries to enter their Credential!!!')
userName = input('Enter your User Name: ')
pwd = input('Enter your Password: ')
counter = 0
while counter < 2:
    if userName == 'Dhara' and pwd == '1234':
        print('Hello ', userName)
        break               
    else:
        userName = input('Enter your Username again: ')
        pwd = input('Enter your Password agian: ')
        counter += 1
    print('Sorry, Exceeded 3 attempts!!')

# 6.

fileName = open('doc.txt','r')
line = fileName.read()
for word in line.split():
    if len(word) % 2 == 0:
        print(word)
fileName.close