class Solution:
    def minimumCoins(self, prices ) :
        n=len(prices)
        memo={}
        def dp(i):
            if i>=n+1:return 0
            if i in memo:return memo[i]
            
            minm=float('inf')
            for j in range(i+1,2*i+2):
                minm=min(minm,dp(j))
            
            memo[i]= minm+prices[i-1]
            return memo[i]
                
        return dp(1)
            

s=Solution()
print(s.minimumCoins([1,10,1,1]))