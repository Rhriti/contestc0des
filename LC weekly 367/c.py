import bisect

def findIndices(nums, idiff,vd):
    arr=[]
    for i in range(len(nums)):
        arr.append([nums[i],i])
    arr.sort()
    indexes=[]
    for ele in arr:indexes.append(ele[1])
    maxm=[indexes[-1] for _ in range(len(nums))]
    minm=[indexes[-1] for _ in range(len(nums))]
    for i in range(len(indexes)-2,-1,-1):
        maxm[i]=max(maxm[i+1],indexes[i])
        minm[i]=min(minm[i+1],indexes[i])
    
    nums.sort()
    final=[-1,-1]
    for i in range(len(nums)):
        nxt=nums[i]+vd
        index=bisect.bisect_left(nums,nxt)
        if 0<=index<len(nums):
            if abs(maxm[index]-indexes[i])>=idiff :
                final[0]=indexes[i]
                final[1]=maxm[index]
                break
            if abs(minm[index]-indexes[i])>=idiff:
                final[0]=indexes[i]
                final[1]=minm[index]
                break
    return final
                

print(findIndices([45,6,33,2,45,9,49,45,24,15,31,0,41,39,30,36,32],
8,
40))