import math
c = 50
h = 50
d = (input('Enter values of D in a Comma (,) separated sequence. '))
result = []
x = d.split(',')
for i in x:
    q = round(math.sqrt(2 * c * int(i) / h))
    result.append(q)
print(result)