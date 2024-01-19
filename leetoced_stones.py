class Solution:
    def minimumMoves(self, grid ) :
        arr=[]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    arr.append([r,c])
        
        tm=0
        for r,c in arr:
            st=[[r,c]]
            m=0
            v={(r,c)}
            for _ in range(4):
                m+=1
                t=[]
                f=False
                while st:
                    out=st.pop()
                    rnew=out[0]
                    cnew=out[1]
                    for x,y in [[rnew+1,cnew],[rnew-1,cnew],[rnew,cnew+1],[rnew,cnew-1]]:
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in v:
                            v.add((x,y))
                            
                            if grid[x][y]>1 :
                                f=True
                                grid[r][c]=1
                                grid[x][y]-=1
                                tm+=m
                                break
                                
                            t.append([x,y])
                    if f:
                        break
                if f:
                    break
                            
                st=t
                
                
                
        return tm
x=Solution()
print(x.minimumMoves([[3,2,0],[0,1,0],[0,3,0]]))