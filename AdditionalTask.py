# 1. Creat a list of given structure and get the Access list as provided below.

x = [100, 200, 300,400, 500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

# Access List: [1,2,3,4]
print(x[5][0:4])

#Access List: [600,700]
print(x[6:8])

#Access List: [100,300,500,600,800]
print(x[0],x[2],x[4],x[6],x[8])
# or 
print(x[::2])

#Access List: Reverse List
print(x[::-1])

#Access List: [10]
print(x[5][5][0])

# 2. Creatr a list of thousand numbers using range and x-range and see the difference between each other.

lst = range(1001)
print(lst)
#lst1 = xrange(1001)--------> Works only in Python 2.x; Not in Python 3.

# 3. How Tuple is beneficial as compared to the list?
# Tuple are stored in a single block of memory. It doesn't require extra space  to store it. 
# Therefore, processing a tuple is a faster than a list.

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the 
# string with their index.

stg = 'ConsultADD'
rvs_stg = stg[::-1]
for i in rvs_stg:
    if i == 'a' or i == 'e' or i =='i' or i == 'o' or i == 'u':
        index = stg.index(i)
        print(index,i)

# 4. Write a program in Python to iterate through the list of numbers in the range of 1 to 100 and 
# print the number which is divisiable by 3 and is a multiple of 2. 
for i in range(1,100):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

# 6.
stg = input('Enter String: ')
s = stg.split(' ')
for i in s:
    if len(i) % 2 == 0:
        print(i)
    else:
        print('Not even length.')

# 7.
x = [1,2,3,4,5,6,7,8,9,-1]
for i in x:
    for j in x[1:]:
        if i+j == 8:
            print(i,j)

# 8.

even_list = []
odd_list = []
even_sum = 0
odd_sum = 0

while (len(even_list) < 5 or len(odd_list) < 5):
    userEnter = int(input('Enter a number between 1 to 50: '))
    if userEnter % 2 == 0:
        if len(even_list)>= 5:
            print('Even list has 5 elements already!')
        else:
            even_list.append(userEnter)
    else:
        if len(odd_list)>=5:
            print('Odd list has 5 elements already!')
        else:
            odd_list.append(userEnter)

for i in even_list:
    even_sum += i

for i in odd_list:
    odd_sum += i

print('Even list: ', even_list)
print('Sum of Even list: ', even_sum)
print('Odd list: ', odd_list)
print('Sum of Odd list: ', odd_sum)

#9.
occurence = { }
stg = input('Enter AlphaNumeric String: ')

for i in stg:
    if i.isalpha():
        if i in occurence:
            occurence[i]+=1
        else:
            occurence[i] = 1
print('Occurence of a Character: ', occurence.items())

#10.
tup = (1,2,3,4,5,6,7,8,9,10)
eTup = []
for i in tup:
    if i % 2 ==0:
        eTup.append(i)
print(tuple(eTup))
