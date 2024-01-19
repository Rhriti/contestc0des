n=int(input())
row=[0 for _ in range(n)]
col=[0 for _ in range(n)]
g=[]
for j in range(n):
    s=input()
    g.append(s)
    for i in range(n):
        if s[i]=='o':col[i]+=1;row[j]+=1
final=0
for r in range(n):
    for c in range(n):
        if g[r][c]=='o':
            final+=(row[r]-1)*(col[c]-1)
print(final)