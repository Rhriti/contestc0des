row,col=map(int,input().split())
g=[]
for _ in range(row):g.append(input())
import sys
sys.setrecursionlimit(row*col)

def dfs(i,j):
    # v.add((i,j))
    for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1],[i+1,j+1],[i-1,j-1],[i+1,j-1],[i-1,j+1]]:
        if   0<=x<row  and 0<=y<col and (x,y) not in v and g[x][y]=='#':
            v.add((x,y))
            dfs(x,y)

v=set()
count=0
for r in range(row):
    for c in range(col):
        if (r,c) not in v and g[r][c]=='#':
            v.add((r,c))
            count+=1
            dfs(r,c)
print(count)

