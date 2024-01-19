#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        memo={}
        def dp(sums,index):
            if (sums,index) in memo:
                return memo[(sums,index)]
            if sums==0:
                return 1
            if sums<0:
                return 0
            if index==len(coins):
                return 0
    
            ways=0
            while sums>=0:
                ways+=dp(sums,index+1)
                sums-=coins[index]
            
            memo[(sums,index)]=ways
            return ways
        
        return dp(Sum,0)
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends