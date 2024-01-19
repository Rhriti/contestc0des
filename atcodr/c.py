n,m=map(int,input().split())
fw=list(map(int,input().split()))
final=[0]*(n+1)

for i in range(len(fw)-1):
    curr=fw[i]
    nxt=fw[i+1]
    for j in range(curr+1,nxt):
        final[j]=nxt-j
for j in range(fw[0]):
    final[j]=fw[0]-j
for i in range(1,len(final)):
    print(final[i])