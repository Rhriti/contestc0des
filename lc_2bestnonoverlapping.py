import bisect
from collections import defaultdict

def m( events ):
    #since here endtime is 10**9 we cant use dp on this
    #hence use dp on events
    events.sort(key=lambda x:x[1])
    et=[events[i][1] for i in range(len(events))]
    maxele=defaultdict(int)
    maxm=float('-inf')
    for ele in events:
        maxm=max(maxm,ele[2])
        maxele[ele[1]]=max(maxele[ele[1]],maxm)
    print(maxele)

    for i in range(len(events)-1,-1,-1):
        s=events[i][2]
        index=bisect.bisect_left(et,events[i][0])
        s+=maxele[et[index-1]]
        maxm=max(s,maxm)
    return maxm
print(m([[1,3,2],[4,5,2],[2,4,3]]))