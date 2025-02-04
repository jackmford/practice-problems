class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Level by level BFS
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        res = 0
        fresh = 0

        # Find all rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            # Process all rotten oranges level at a time
            qLen = len(q)

            for i in range(qLen):
                cur = q.popleft()
                x, y = cur[0], cur[1]
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    q.append((x-1, y))
                    fresh-=1
                if x < ROWS-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    q.append((x+1, y))
                    fresh-=1
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    q.append((x, y-1))
                    fresh-=1
                if y < COLS-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    q.append((x, y+1))
                    fresh-=1
            res+=1

        return res if fresh == 0 else -1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is a level by level traversal from every "2"

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        ctr = 0
        while fresh > 0 and q:
            qLen = len(q)
            print(qLen)
            print(grid)

            for _ in range(qLen):
                cur = q.popleft()
                if cur in visited:
                    continue
    
                visited.add(cur)
                r, c = cur[0], cur[1]
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append((r-1, c))
                    fresh-=1
                if r < ROWS-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append((r+1, c))
                    fresh-=1
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append((r, c-1))
                    fresh-=1
                if c < COLS-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append((r, c+1))
                    fresh-=1
                # Process cur's neighbors
            ctr+=1

        if fresh > 0:
            return -1
        return ctr
