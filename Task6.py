#1. Write a program in Python to find out the character in a string 
# which is uppercase using list comprehension.

stg = 'Hello World!!! Have a Gread day!'

result = [i for i in stg if i.isupper()]
print('String is: ', stg, ' and Uppercase Characters in String are: ',result)


#2. Loopand Dictionary comprehension.

student = ['Smit','Jaya','Rayyan']
subject = ['CSE', 'Networking','Operating System']
mapDict = dict(zip(student,subject))
print(mapDict)

#4. REverse the string using Generator.

def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

for string in reverse_string('Python Programming'):
    print(string)