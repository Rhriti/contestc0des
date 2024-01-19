from collections import defaultdict

def longestEqualSubarray( nums , k ) :
    f=defaultdict(int)
    s=defaultdict(lambda:float('inf'))
    e=defaultdict(lambda: -float('inf'))
    for i in range(len(nums)):
        f[nums[i]]+=1
        s[nums[i]]=min(s[nums[i]],i)
        e[nums[i]]=max(e[nums[i]],i)
    arr=[]
    for j in f.keys():
        arr.append([ f[j] , e[j]-s[j]+1-f[j] ])
    arr.sort(reverse=True)
    print(arr)
    for ele in arr:
        if ele[1]<=k:
            return ele[0]
print(longestEqualSubarray([3,1,5,3,1,1],
0))