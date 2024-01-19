ranges=[[0,10],[11,34],[35,44],[56,100]]
n=100
h=len(ranges)-1
l=0
while l<=h:
    print(l,h)
    mid=(l+h)//2
    if ranges[mid][0]<=n<=ranges[mid][1]:
        print(mid)
        break
    elif n<ranges[mid][0]:
        h=mid-1
    else:
        l=mid+1
