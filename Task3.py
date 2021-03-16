# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

x = [1,2,3,'Hello', 'Hi', 4.5, 6.5, 1+2j,1j,'Hey!']
print(x)

#-----------------------------------------------------------------------
# 2. Create a list of size 5 and execute the slicing structure

x   # Original List 
x1 = x[:3] # Starting element to elemrnt 2
print(x1)
x2 = x[6:]  # Element 6 to end
print(x2)
x3 = x[3:6] # Element 3 to 5
print(x3)

#-----------------------------------------------------------------------------
# 3. Writea program to get the sum and multiply of all the items in a given list.

y = [1,2,3,4,5] # Original List 1
add = 0
mul = 1
for i in range(len(y)):
    add = add + y[i]
    mul = mul * y[i]
print('Addition of all items in a given list: ', add)
print('Multiplication of all items in a given list: ', mul)

#--------------------------------------------------------------------------------
# 4. Find the largest and smallest number from a given list.

y = [44,22,54,78,67,42,53,32,54,76,32,43,11]
print(min(y))   # Minimum number of a given list
print(max(y))   # Maximum number of a given list

# --------------------------------------------------------------------------------
# 5. Create a new list which contains the specified numbers 
# after removing the even numbers from apredefined list.

p = [32,86,88,33,11,34,5,43,35,56,39,89]
new_p = []
for i in range(len(p)):
    if p[i] % 2 != 0:
        new_p.append(p[i])
print(new_p)

#----------------------------------------------------------------------------------
# 6. Create a list of elements such that it contains
# the squares of the first and last 5 elements between 1 and 30 (both included).

lst = []
for i in range(1,6):
    lst.append(i**2)
for i in range(26,31):
    lst.append(i**2)
print(lst)

#------------------------------------------------------------------------------------
# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10],[2,4,6,8] Expected output: [1,3,5,7,9,2,4,6,8]

a = [1,3,5,7,9,10]
b = [2,4,6,8]
a[-1:] = b
print(a)

#-------------------------------------------------------------------------------------
# 8. Create a new dictionary by concatenating the following two dictionaries: 
# Sample input:a={1:10,2:20} b={3:30,4:40} Expected output: {1:10,2:20,3:30,4:40}

a = {1:10,2:20}
b = {3:30,4:40}

a.update(b)
print(a)

#---------------------------------------------------------------------------------------
# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes 
# all the values between 1 and n(both 1 and n included). 
# Sample input:n=5 Expected output: {1:1, 2:4, 3:9, 4:16, 5:25} 

x = {}
for i in range(1,11):
    x[i] = i ** 2
print(x)

#---------------------------------------------------------------------------------------
# 10. Write a program which accepts a sequence of comma-separated numbers from console 
# and generates a list and a tuple which contains every number in the form of string.

lst = []
tpl = ()

stg = input('Enter a string: ')
lst.append(stg)
tpl = tuple(lst)
print('List is: ', lst)
print('Tuple is: ', tpl)
