class Solution:
    def minimumMoves(self, grid ) :
        arr=[]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    arr.append([r,c])
        
        tm=0
        for r,c in arr:
            steps=0
            st=[[r,c]]
            v={(r,c)}
            while grid[r][c]!=1:
                steps+=1
                t=[]
                while st:
                    
                    out=st.pop()
                    rnew=out[0]
                    cnew=out[1]
                    f=False
                    for x,y in [[rnew+1,cnew],[rnew-1,cnew],[rnew,cnew+1],[rnew,cnew-1]]:
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in v:
                            v.add((x,y))
                            if grid[x][y]>1:
                                f=True
                                tm+=steps
                                grid[r][c]=1
                                grid[x][y]-=1
                                break
                                
                            t.append([x,y])
                    if f:
                        break
                st=t
                    
            
            return tm
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            