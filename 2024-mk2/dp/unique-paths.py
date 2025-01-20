class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            print(i, j)
            if cache[i][j] != -1:
                return cache[i][j]
            if i == m-1 and j == n-1:
                return 1
            
            # Go down
            down = 0
            if i < m-1:
                down += dfs(i+1, j)

            # Go right
            right = 0
            if j < n-1:
                right += dfs(i, j+1)
            
            cache[i][j] = down+right

            return down+right

        return dfs(0, 0)
        
