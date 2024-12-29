class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()
        

        def dfs(row, col, i):
            # We went far enough to find a match
            if i == len(word):
                return True

            # Base cases
            # Don't explore these paths
            if row < 0 or col < 0:
                return False
            if row >= len(board):
                return False
            if col >= len(board[0]):
                return False
            if word[i] != board[row][col]:
                return False
            # Already visited
            if (row, col) in path:
                return False
            
            # Add node to path
            path.add((row,col))

            # Look for a path in every direction
            up = dfs(row-1, col, i+1)
            down = dfs(row+1, col, i+1)
            left = dfs(row, col-1, i+1)
            right = dfs(row, col+1, i+1)

            # Node explored
            path.remove((row, col))

            return up or down or left or right

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
                    
        return False



