class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # if island is land and neighbor is out of bounds or water, +1
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0

        def dfs(i, j):
            nonlocal perimeter
            if i < 0 or i >= ROWS:
                return 1
            if j < 0 or j >= COLS:
                return 1
            if grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i,j))
            
            down = dfs(i+1, j)
            up = dfs(i-1, j)
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            
            return down+up+right+left

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    print(i,j)
                    return dfs(i,j)

        
