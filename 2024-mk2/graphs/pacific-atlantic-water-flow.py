class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # For any node we want to know if we can reach either the left or top edge AND the right or bottom edge

        ROWS,COLS = len(heights), len(heights[0])
        res = []
        atl, pac = set(), set()

        # From edge nodes, find neighbors that are >= starting node
        # This will find nodes that can visit edges
        def dfs(x,y, visit):
            if (x,y) in visit:
                return

            # Not visited and in bounds,
            # was >= previous node
            visit.add((x,y))
            if x > 0:
                if heights[x-1][y] >= heights[x][y]:
                    dfs(x-1, y, visit)
            if x < ROWS-1:
                if heights[x+1][y] >= heights[x][y]:
                    dfs(x+1, y, visit)
            if y < COLS-1:
                if heights[x][y+1] >= heights[x][y]:
                    dfs(x, y+1, visit)
            if y > 0:
                if heights[x][y-1] >= heights[x][y]:
                    dfs(x, y-1, visit)

        # Left and right side
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)
        # Top and bottom side 
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS-1, c, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res

            
            

