
def minOperations(nums1 , nums2 ):
    #not possible
    endmax=max(nums1[-1],nums2[-1])
    endmin=min(nums1[-1],nums2[-1])
    for i in range(len(nums1)-1):
        if nums1[i]>endmin and nums2[i]>endmin:
            return -1
        if max(nums1[i],nums2[i])>endmax:
            return -1
    if endmin==endmax:return 0
    
    up=0
    down=0
    count=0
    for i in range(len(nums1)-1):
        if nums1[i]>endmin:up+=1
        if nums2[i]>endmin:down+=1
    if up==down:
        return up
    elif up<down:
        count+=up
        if nums2[-1]==endmax:return count
        else:return count+1
    else:
        count+=down
        if nums1[i]==endmax:return count
        else:return count+1
        
        
        
        
        
minOperations([1,5,15]
,[1,1,1])
        
    