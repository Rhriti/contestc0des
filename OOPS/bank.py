class Bank:
    def __init__(self,bal):
        self.bal=bal
        self.__pin=None  #private attribute
    def show(self):
        return self.bal
    def changepin(self,pin):
        self.__pin=pin
        print('success')
    def __rich(self):
        if self.bal>1000:
            print('rich')
        else:
            print('poor')
        return 'fk u'


sbi=Bank(999)
sbi.changepin(123)
print(sbi.show())
print(sbi._Bank__rich())
#
sbi.__pin=1000
print(sbi.__pin)
#above code still works
# this is because earlier atribute of __pin beccame _Bank__pin and __pin doesn't exist anymore untill now.abs 


