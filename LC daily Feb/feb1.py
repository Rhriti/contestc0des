import bisect 
class Solution:
    def divideArray(self,nums , k ):
        nums.sort()
        i=0
        f=True
        final=[]
        while i<len(nums):
            index=bisect.bisect_right(nums,nums[i]+k)
            l=index-i
            if l>=3:
                final.append([nums[i],nums[i+1],nums[i+2]])
                i+=3
            else:
                f=False
                break
        if f:
            print(final)

    

