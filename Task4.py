# 1. Write a program to reverse a string.

stg = input('Enter String: ')
rvs_stg = stg[::-1]
print(rvs_stg)

# 2. Write a function that accepts a string and prints 
# the number of uppercase letters and lowercase letter.

stg = input('Enter mixter of uppercase and lowercase String: ')
upperCase = 0
lowerCase = 0
for i in stg:
    if i.islower():
        lowerCase += 1
    else:
        upperCase += 1

print('No of UpperCase is: ', lowerCase)
print('No of LowerCase is: ', lowerCase)

# 3. Create a function that takes a list and returns a new list 
# with unique elements of the first list.

lst = ['1', '2', '3', '4', '5', '6', '3', '4', '4', '5', '6', '1']
lst1 = set(lst)
print(lst1)

# 4.  Write a program that accepts a hyphen-separated sequence of 
# words as input and prints the words in a hyphen-separated sequence 
# after sorting them alphabetically.

stg = 'H-E-L-L-O-!'
stg1 = stg.split('-')
print(sorted(stg1))

# 5. Write a program that accepts a sequence of lines as input and 
# prints the lines after making all characters in the sentence capitalized.

stg = input('Enter a String: ')
stg1 = stg.upper()
print(stg1)

# 6. Define a function that can receive two integral numbers in string form 
# and compute their sum and print it in the console.

def sum(a,b):
    add = int (a) + int(b)
    return add

print(sum(8,16))

# 7. Define a function that can accept two strings as input and print the 
# string with the maximum length in the console. If two strings have the 
# same length, then the function should print both the strings line by line.

def maxStg(stg1,stg2):
    if (len(stg1) > len(stg2)):
        return stg1
    elif (len(stg1) < len(stg2)):
        return stg2
    else:
        return stg1, stg2

print(maxStg('ABCD','ABCDE'))
print(maxStg('ABC','ABC'))
print(maxStg('ABC','ABCD'))

# 8. Define a function which can generate and print a tuple where the values 
# are square of numbers between 1 and 20 (both 1 and 20 included).

def tup():
    lst = []
    for x in range(1,21):
        x = x**2
        lst.append(x)
    return tuple(lst)

print(tup())

# 9. Write a function called showNumbers that takes a parameter called limit.
#  It should print all the numbers between 0 and limit with a label to identify 
# the even and odd numbers.

def showNumbers(limit):
    x = int(limit)
    for i in range(x+1):
        if i%2 != 0:
            print('Odd Number: ', i)
        else:
            print('Even Number: ', i)

print(showNumbers(2))
print(showNumbers(5))

# 10. Write a program which uses filter() to make a list whose elements are even
# numbers between 1 and 20 (both included)

r = range(1,21)
lst = list(filter(lambda x:x%2==0,r))
print(lst)

# 11. Write a program which uses map() and filter() to make a list whose elements 
# are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].

x = range(1,11)
lst = list(map(lambda x:x**2, filter(lambda x:x%2==0,x)))
print(lst)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def zdiv(x,y):
    try:
        a = x/y
        return a
    except ZeroDivisionError:
        print('Zero Division Error.')
    except:
        print('Other Error Occured.')

zdiv(5,0)

# 13. Flatten the list[1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce

y = reduce(lambda a,b:10*a+b,[1,2,3,4,5,6,7])
print(y)

# 14. Write a program in Python to find the values which are not divided by 3 but
#  are a multiple of 7. Mak sure to use only higher order functions.

lst = list(filter(lambda: x:x%3!=0 and x%7==0, range(25)))
print(lst)

# 15. Write a programm in Python to multiply the elements of a list by itself using a 
# traditional function and pass the function to map() to complete the operation.

def multipleList(num):
    return num**2

lst = [1,2,3,4,5,6]
mul = list(map(multipleList,lst))
print(mul)

# 16.(i)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()        
print(k)

####### Result: 2

# 16.(ii)
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

###### Result: NameError: 'f' is not defined.