#User function Template for python3
class Solution:
    def __init__(self):
        self.memo={}
        
	def minJumps(self, arr, n):
	 
	    #themost obvioius 
	    def dp(index):
	        if index==len(arr)-1:
	            return 0
	        if index in self.memo:
	            return self.memo[index]
	            
	        minm=float('inf')
	        for i in range(index+1,min(index+arr[index]+1,len(arr))):
	            minm=min(minm,1+dp(i))
	        self.memo[index]=minm
	        return minm
	        
	    ans=dp(0)
	    return ans if ans!=float('inf') else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends