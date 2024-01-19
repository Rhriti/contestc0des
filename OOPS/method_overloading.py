class X:
    def show(self,x):
        return x
    def show(self):
        return 'wtf'

x=X()
print(x.show(1))