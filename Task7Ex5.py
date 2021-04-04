class person:
    age = 0
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Age is not valid, seting age to 0')
            self.age = 0
        else:
            self.age = initialAge

    def yearPasses(self,initialAge):
        print('After ', initialAge, 'Increased Age is: ', self.age + initialAge)
    
    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age <= 19:
            print('You are teenager.')
        else:
            print('You are Old.')

a = int(input('Number of inputs: '))
for i in range(1, 1 + a):
    j = int(input('Enter Age: '))
    output = person(j)
    output.yearPasses(4)
    output.amIOld()