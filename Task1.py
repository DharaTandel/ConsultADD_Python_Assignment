#______ConsultADD INC______
#_______Assignment 1_______
#__________Task 1__________

# 1. Create three variable in a sngle line
x,y,z = 8, 1.6, 'Python' 
print('Variable x is: ', x) # int
print("Variable y is: ", y) # float
print("Variable z is: ", z) # string

# 2. Create a variable of type complex and swap it woth another variable of type integer
a = 8j
print(type(a))  # Complex
b = 5
print(type(b))  # Int
c = b   #  c is a dummy variable for swipe
b = a
a = c
print("a is ", a, "b is ", b)

# 3. Swap two numbers using a third variable and do the same task without using any third variable.
# Swap two numbers using a third variable
# V1 = 3 and V2 = 5
# Result should be V1 = 5 and V2 = 3 
V1 = 3
V2 = 5
t = V1
V1 = V2
V2 = t
print("Value of V1 and V2 are: ", V1, V2, "respectively.")

# Swap two numbers without third variable
# From 1 x = 8 and y = 1.6
# Result should be x = 1.6 and y = 8
x, y = y,x
print(x,y)

# 4. Input takes from the user and prints it using both Python 2.x and Python 3.x Version.
# Python 3.x
number1 = input("Enter the value of number1: ")
print("Number 1 is in Python 3.x:", number1)

#Python 2.x
number2 = eval(raw_input("Enter the value of number2: "))
print("Number 2 is in Python 2.x:", number2)

# 5. Ask users to enter any 2 numbers in between 1-10 , 
# add the two numbers and keep the sum in another variable called z. 
# Add 30 to z and store the output in variable result and print result as the final output.

x = int(input("Enter the 1st number between 1-10: "))
y = int(input("Enter the 2nd number between 1-10: "))
z = x + y
result = z + 30
print("Result is:", result)

# 6. The data type of the entered values.
i = 3
j = 8.5
k = 2j
l = 'ConsultADD'
print("The data type of i is: ", type(i))
print("The data type of j is: ", type(j))
print("The data type of k is: ", type(k))
print("The data type of l is: ", type(l))

# 7. Create Variables using formats 
# such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

#UpperCamelCase
FirstName = 'Dhara'

#LowerCamelCase
firstName = 'Dhara'

#Snake Case
first_name = 'Dhara'

#UPPER Case
FIRSTNAME = 'DHARA'

#-----------------------------------------------------
# 8. If one data type value is assigned to variable 
# and then a different data type value is assigned to variable again. 
# Will it change the value? If Yes then Why?
#ANSWER: YES, Variables in Python can contain different type of 
# data types such as int, str, float, etc. When you assign a value to variable that will store in it. 
# If you reassign a value to same variable and different data type then it will empty out old value and the new value will be placed inside of it.
