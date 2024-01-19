n,m,k=map(int,input().split())
nodes=set()
print(nodes)
arr=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    arr.append([w,u,v])
arr.sort()
arr=arr[::-1]
count=0
print(arr)
while len(nodes)!=n:
    w,u,v=arr.pop()
    if u in nodes and v in nodes:
        continue
    else:
        nodes.add(u)
        nodes.add(v)
        count+=w
print('ans',count%k)

