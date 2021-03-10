#-----------3. FlowChart-----------------

a = int (input("Enter the value of a: ")) 
b = int (input("Enter the value of b: ")) 
c = int (input("Enter the value of c: "))

avg = (a + b + c)/3
print("Average is: ", avg)

if ((avg>a) and (avg>b) and (avg>c)):
    print("Average is higher than a, b and c.")
elif ((avg>a) and (avg>b)):
    print("Average is higher than a and b.")
elif ((avg>a) and (avg>c)):
    print("Average is higher tahn a and c.")
elif((avg>c) and (avg>b)):
    print("Average is higher than b and c.")
elif (avg>a):
    print("Average is just higher than a.")
elif (avg>b):
    print("Average is just higher than b.")
else:
    print("Average is just higher than c.")
