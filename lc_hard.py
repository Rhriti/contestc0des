from collections import deque,defaultdict
import math
class Solution:
    def ps(self,n):
        s=set()
        while n%2==0:
            s.add(2)
            n=n/2
        for ele in range(3,int(math.sqrt(n))+1):
            while n%ele==0:
                s.add(ele)
                n=n/ele
        if n!=1:
            s.add(n)
        return len(s)
    
    def maximumScore(self, nums , k ):
        nger=[len(nums) for _ in range(len(nums))]
        s=[]
        arr=[]
        for i in range(len(nums)):
            arr.append([-nums[i],i])
            if len(s)==0:
                s.append([self.ps(nums[i]),i])
            else:
                while s and s[-1][0]<self.ps(nums[i]):
                    out=s.pop()
                    nger[out[1]]=i
                s.append([self.ps(nums[i]),i])
        arr.sort()
        ngel=[None for _ in range(len(nums))]
        s=[]
        for i in range(len(nums)-1,-1,-1):
            if len(s)==0:
                s.append([self.ps(nums[i]),i])
            else:
                while s and s[-1][0]<=self.ps(nums[i]):
                    out=s.pop()
                    ngel[out[1]]=i
                s.append([self.ps(nums[i]),i])
        ans=1
        for ele in arr:
            r=nger[ele[1]]
            l=ngel[ele[1]]
            R=r-ele[1]
            if l is not None:
                L=ele[1]-l
            else:
                L=ele[1] if ele[1]!=0 else 1
            t=L*R
            if t<=k:
                ans=ans*(-ele[0])**t
                k-=t
            else:
                ans*=(-ele[0])**k
                k=0
        print(ans)
        return ans
            
x=Solution()
x.maximumScore([19,12,14,6,10,18],3)
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            
        
        