class time:
    def __init__(self,hrs,mins):
        self.hrs = hrs
        self.mins = mins

    def addTime(t1,t2):
        t3 = time(0,0)
        if t1.mins + t2.mins > 60:
            t3.hrs = (t1.mins + t2.mins)/60
        t3.hrs = t1.hrs + t2.hrs + t3.hrs
        t3.mins = (t1.mins + t2.mins) - ((t1.mins + t2.mins)/60)
        return t3
    
    def displayTime(self):
        print('Time is: ', self.hrs, 'hours and ', self.mins, 'mins')

    def displayMinute(self):
        print(self.hrs * 60 + self.mins)

tym1 = time(1,20)
tym2 = time(2,50)
result = time.addTime(tym1,tym2)
result.displayTime()
result.displayMinute()