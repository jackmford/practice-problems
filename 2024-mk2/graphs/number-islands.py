class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Start at 0,0 if point == "1", set it to "0" and call dfs on it's neighbors
        # When you reach no more neighbors with "1" return a +1
        # Find the next cell that isn't a 1 and start dfs again

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(x, y):
            print(x, y)
            if grid[x][y] == "0":
                return 0

            grid[x][y] = "0"

            if x > 0:
                dfs(x-1, y)
            if x<ROWS-1:
                dfs(x+1, y)
            if y<COLS-1:
                dfs(x, y+1)
            if y > 0:
                dfs(x, y-1) 
            
            return 1
        total = 0
        for x in range(ROWS):
            for y in range(COLS):
                total += dfs(x, y)

        return total
