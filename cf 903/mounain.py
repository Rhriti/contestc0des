# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


def findInMountainArray(target , mountain ) :
    i=0
    j=len(mountain)-1
    while j-1>1:
        mid=(i+j)//2
        
        l=mid-1
        r=mid+1
        
        left=mountain[l]
        right=mountain[r]
        middle=mountain[mid]
        if left<middle>right:
            break
        elif right>middle>left:
            i=mid
        else:
            j=mid
    beech=mid
    print('mid',beech)
    i=0
    j=beech
    while i<=j:
        mid=(i+j)//2
        middle=mountain.get(mid)
        if middle==target:
            return mid
        elif middle>target:
            j=mid-1
        else:
            i=mid+1
    
    i=beech
    j=mountain.length()-1
    while i<=j:
        mid=(i+j)//2
        middle=mountain.get(mid)
        if middle==target:
            return mid
        elif middle>target:
            i=mid+1
        else:
            j=mid-1
    return -1

print(findInMountainArray(0,[1,2,3,5,3]
))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
    