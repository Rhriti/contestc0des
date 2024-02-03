
def maximumSubarraySum(nums , k ):
    pres=[nums[0]]
    for i in range(1,len(nums)):pres.append(pres[-1]+nums[i])
    g={nums[0]:0}
    maxm=-float('inf')
    f=False

    for i in range(1,len(nums)):
        prev1=nums[i]+k
        prev2=nums[i]-k
        if prev1 in g:
            f=True
            maxm=max(maxm,pres[i]-pres[g[prev1]]+nums[g[prev1]])

        if prev2 in g:
            f=True
            maxm=max(maxm,pres[i]-pres[g[prev2]]+nums[g[prev2]])
        
        if nums[i] in g:
            prev_index=g[nums[i]]
            sums=pres[i-1]-pres[prev_index]+nums[prev_index]
            if sums>0:pass
            else:g[nums[i]]=i
           
    
    if f:return maxm
    else:return 0
        
    
print(maximumSubarraySum([3,3,2]
,1))
    