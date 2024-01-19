from collections import deque

def nextGreaterElements( nums ):
    s=deque()
    s.append([nums[0],0])
    i=1%len(nums)
    g={}
    while s:
        if s[0][1]==i:
            out=s.popleft()
            g[out[1]]=-1
        
        while s and s[-1][0]<nums[i]:
            out=s.pop()
            g[out[1]]=nums[i]
        if i not in g:
            s.append([nums[i],i])
        i=(i+1)%len(nums)
    final=[]
    for i in range(len(nums)):
        final.append(g[i])
    return final

print(nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))            
            
    