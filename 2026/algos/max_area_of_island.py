class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}

        def dfs(i, j):
            if i < 0:
                return 0
            if j < 0:
                return 0
            if i >= len(grid):
                return 0
            if j >= len(grid[0]):
                return 0
            if (i, j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited[(i, j)] = 1

            right = dfs(i + 1, j)
            left = dfs(i - 1, j)
            down = dfs(i, j + 1)
            up = dfs(i, j - 1)

            return right + left + down + up + 1

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
