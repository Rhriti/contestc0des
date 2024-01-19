class Fraction:
    def __init__(self,n,d):
        self.n=n
        self.d=d
    
    def __str__(self):
        return f'{self.n}/{self.d}'
    def __add__(self,other):
        adds=(self.n/self.d)+(other.n/other.d)
        return adds

a=Fraction(2,3)
b=Fraction(4,5)
a.new=44
print(a.new)
print(a+b)