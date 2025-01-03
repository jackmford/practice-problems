class Solution: 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        ones=0
        total = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    ones+=1
        while ones>0 and len(q) > 0:
            qLen = len(q)
            for i in range(qLen): 
                orange = q.popleft()
                x,y = orange[0], orange[1]
                if x-1 in range(ROWS) and y in range(COLS) and grid[x-1][y] == 1:
                    ones-=1
                    grid[x-1][y] = 2
                    q.append((x-1, y))
                if x+1 in range(ROWS) and y in range(COLS) and grid[x+1][y] == 1:
                    ones-=1
                    grid[x+1][y] = 2
                    q.append((x+1, y))
                if x in range(ROWS) and y-1 in range(COLS) and grid[x][y-1] == 1:
                    ones-=1
                    grid[x][y-1] = 2
                    q.append((x, y-1))
                if x in range(ROWS) and y+1 in range(COLS) and grid[x][y+1] == 1:
                    ones-=1
                    grid[x][y+1] = 2
                    q.append((x, y+1))
            total+=1

        if ones > 0:
            return -1
        return total


