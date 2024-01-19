class X:
    def show(self,x):
        return x
    
class Y(X):
    def show(self):
        return 'wtf man'

y=Y()
print(y.show(99))
    