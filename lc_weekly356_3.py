from collections import defaultdict

def maximumSafenessFactor(grid ) :
    ones=[]
    zeros=[]
    sf=defaultdict(int)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                ones.append([r,c])
            else:
                zeros.append((r,c))
    for ele in zeros:
        minm=float('inf')
        for x,y in ones:
            minm=min(minm,abs(x-ele[0])+abs(y-ele[1]))
        sf[ele]=minm
    memo={}
    visit=set()
    def f(r,c) :
        visit.add((r,c))
        if r==len(grid)-1 and c==len(grid)-1:
            return sf[(r,c)]
        if (r,c) in memo:
            return memo[(r,c)]
        maxm=-float('inf')
        for x,y in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
            if 0<=x<len(grid) and 0<=y<len(grid) and (x,y) not in visit:
                maxm=max(maxm,min(sf[(r,c)],f(x,y)))
        memo[(r,c)]=maxm
        print(maxm)
        return maxm
    return f(0,0)
        
        
print(maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])) 
        
        
        
        
        
        
        
        
        
        
        
        
        
    