
class TreeAncestor:

    def __init__(self, n, parent):
        self.parent=parent
        
        self.n=n
        rows=20
        self.memo=[[-1 for _ in range(n)] for _ in range(rows)] #-1 got nothing to do with answers
        for i in range(n):self.memo[0][i]=parent[i]
            
        for j in range(1,rows):
            for i in range(n):
                t=self.memo[j-1][i]
                if t==-1:self.memo[j][i]=-1
                else:self.memo[j][i]=self.memo[j-1][t]
        
    def getKthAncestor(self, node , k ) :
        # print(self.memo)
        binary=bin(k)[2:][::-1]
        for i in range(len(binary)):
            if binary[i]=='1':
                node=self.memo[i][node]
                if node==-1:return -1
        return node
        