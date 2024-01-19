class StockSpanner:
    def __init__(self):
        self.d=[]
    def next(self, price):
        
        ans=1
        for i in range(len(self.d)-1,-1,-1):
            #base
            if self.d[i][0]>price:
                break
            ans+=self.d.pop()[1]
        self.d.append([price,ans])
        return ans