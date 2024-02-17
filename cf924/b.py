
from collections import deque
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    newarr=[arr[i]-arr[i-1] for i in range(1,len(arr)) if arr[i]-arr[i-1]!=0]
    target=n-1
  
    st=deque()
    curr_sum=0
    maxl=0
    #using monotonic stack is heck lot easier 

    for i in range(len(newarr)):
        curr_sum+=newarr[i]
        st.append(newarr[i])

        if curr_sum>target:
            while curr_sum>target:
                out=st.popleft()
                curr_sum-=out
                
        maxl=max(maxl,len(st))
    
    print(maxl+1)
        

    







        
        