class X:
    counter=0 #class variable are same for all instances of the class
    def __init__(self,name):
        self.name=name  #instance variable are different for all different instance of class
        X.counter+=1
        self.roll=X.counter


a=X('Raj')
b=X('king')
print(a.roll)
print(b.roll)
print(a.counter)
print(b.counter)
