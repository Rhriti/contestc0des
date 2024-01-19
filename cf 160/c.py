from collections import defaultdict
g=defaultdict(int)
n=int(input())
arr=[0 for _ in range(30)]
for _ in range(n):
    a,b=map(int,input().split())
    if a==1:
        arr[b]+=1
    else:
        w=b
        f='NO'
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==0:continue
            if arr[i]*2**i>=w:
                f='YES'
                break
                #yes return 
            else:
                w-=arr[i]*2**i 
        print(f)
        
    

