class Smartphone:
    def __init__(self,name,model):
        self.name=name
        self.__model=model

class Xiomi(Smartphone):
    def __init__(self,name,model,price):
        super().__init__(name,model)
        self.price=price
        self.help()
    def help(self):
        print(self.name)
        # print(self.__model)
        print(self.price)


x=Xiomi('KR','001',10000)
# print(x.__model) gives no attribute error