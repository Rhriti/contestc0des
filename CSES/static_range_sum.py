n,m=map(int,input().split())
arr=list(map(int,input().split()))
pres=[]
s=0
for ele in arr:
    s+=ele
    pres.append(s)
for _ in range(m):
    a,b=map(int,input().split())
    print(pres[b-1]-pres[a-1]+arr[a-1])