n=int(input())
from collections import defaultdict,Counter
g=defaultdict(int)
import copy
tempprev=prev=arr=[]

for i in range(n):
    s=list(map(str,input().split()))
    if i==0:
        g[s[1]]+=1
        arr.append(s[1])
        tempprev=arr
    else:
        if len(s)==1:
            if s[0]=='?':
                print(len(g))
            else:
                arr=prev
                g=Counter(arr)
                tempprev=arr

        else:
            if s[0]=='+':
                prev=copy.deepcopy(tempprev)
                g[s[1]]+=1
                arr.append(s[1])
                tempprev=arr
            else:
                prev=copy.deepcopy(tempprev)
                for i in range(len(arr)-1,len(arr)-1-int(s[1]),-1):
                    g[arr[i]]-=1
                    if g[arr[i]]==0:
                        del g[arr[i]]
                arr=arr[:len(arr)-int(s[1])]
                tempprev=arr

