class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def dfs(x,y):
            if grid[x][y] == 0:
                return 0

            grid[x][y] = 0

            total = 0
            if x>0:
                total+=dfs(x-1, y)
            if x<ROWS-1:
                total+=dfs(x+1, y)
            if y>0:
                total+=dfs(x, y-1)
            if y<COLS-1:
                total+=dfs(x, y+1)
            
            return total+1
        
        for r in range(ROWS):
            for c in range(COLS):
                total = dfs(r, c)
                res = max(total, res)
        
        return res

