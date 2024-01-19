n,q=map(int,input().split())
s=input()
qu=[]
for _ in range(q):qu.append(list(map(int,input().split())))
if len(s)==1:
    for _ in range(q):print(0)
else:
    arr=[0 for _ in range(n)]
    for j in range(1,len(s)):
        if s[j]==s[j-1]:arr[j]=arr[j-1]+1
        else:arr[j]=arr[j-1]
    for u,v in qu:
        print(arr[v-1]-arr[u-1])


