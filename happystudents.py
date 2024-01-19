from collections import Counter
from  bisect  import bisect_left

def countWays(nums ) :
    nums.sort()
    g=Counter(nums)
    ans=0
    for size in range(len(nums)+1):
        if g[size]>1:continue 
        else:
            index=bisect_left(nums,size)
            if (index==len(nums)) or (index==size and nums[index]!=size):
                ans+=1
    return ans

print(countWays([6,0,3,3,6,7,2,7]))



    