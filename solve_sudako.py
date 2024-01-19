import copy 
class Solution:
    def __init__(self):
        self.f=False
    def solveSudoku(self, g) :
        self.g=g
        row=[set() for _ in range(len(g))]
        col=[set() for _ in range(len(g[0]))]
        for r in range(len(g)):
            for c in range(len(g[0])):
                if g[r][c]!='.':
                    g[r][c]=int(g[r][c])
                    row[r].add(g[r][c])
                    col[c].add(g[r][c])
        def valid(r,c,ele):
            for i in range(3*(r//3),3*(r//3)+3):
                for j in range(3*(c//3),3*(c//3)+3):
                    if g[i][j]==ele:
                        return False
            return True

        def s(r,c):
            if r==len(g):
                return True
            if c==len(g[0]):
                return s(r+1,0)
            if g[r][c]=='.':
                for ele in range(1,10):
                    if ele not in row[r] and ele not in col[c] and valid(r,c,ele):
                        row[r].add(ele)
                        col[c].add(ele)
                        g[r][c]=ele
                        if s(r,c+1):
                            return True
                        row[r].remove(ele)
                        col[c].remove(ele)
                        g[r][c]='.'
                return False
            else:
                return s(r,c+1)
        s(0,0)

s=Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(s.g)
        
        