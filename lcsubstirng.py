#User function Template for python3

class Solution:
    def __init__(self):
        self.memo={}
        
    def longestCommonSubstr(self, S1, S2, n, m):
        
        def f(i,j):
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            if i<0 or  j<0:
                return 0
                
            if S1[i]==S2[j]:
                t=1+f(i-1,j-1)
                self.memo[(i,j)]=t
                return t
            else:
                self.memo[(i,j)]=0
                return 0
        maxm=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if (i,j) in self.memo:
                    maxm=max(maxm,self.memo[(i,j)])
                else:
                    maxm=max(maxm,f(i,j))
        return maxm

# time complexity of above recursive solution is O(n*m) and space complexity is O(n*m)