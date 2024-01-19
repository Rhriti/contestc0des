class Solution:
    def solveSudoku(self, grid):
        row = [set() for _ in range(len(grid))]
        col = [set() for _ in range(len(grid[0]))]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != '.':
                    row[r].add(grid[r][c])
                    col[c].add(grid[r][c])
        
        def valid(r, c, ele):
            for i in range(3 * (r // 3), 3 * (r // 3) + 3):
                for j in range(3 * (c // 3), 3 * (c // 3) + 3):
                    if grid[i][j] == ele:
                        return False
            return True
        
        def s(r, c):
            nonlocal f  # Declare f as a nonlocal variable
            if r == len(grid):
                f = True
                return 
            
            if grid[r][c] != '.':
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    f = True
                    return 
                if c < len(grid[0]) - 1:
                    s(r, c + 1)
                if c == len(grid[0]) - 1:
                    s(r + 1, 0)
            else:
                for ele in range(1, 10):
                    if ele not in row[r] and ele not in col[c] and valid(r, c, ele) and not f:
                        row[r].add(ele)
                        col[c].add(ele)
                        grid[r][c] = ele
                        if c < len(grid[0]) - 1:
                            s(r, c + 1)
                        if c == len(grid[0]) - 1:
                            s(r + 1, 0)
                        row[r].remove(ele)
                        col[c].remove(ele)
                        grid[r][c] = '.'
        
        f = False  # Initialize f before calling s
        s(0, 0)
        return grid
