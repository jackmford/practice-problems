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

            
            
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # From the top and left side, find any node that can reach the pacific
        # From the right and bottom side, find any node that can reach the atlantic
        # Nodes in both are to be returned

        atlantic, pacific = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(x, y, visited):
            if (x, y) in visited:
                return
            
            # Add the node we are on to the visited set, meaning we can get to this ocean from this node
            visited.add((x,y))
            # Check every direction for more nodes to visit
            if x > 0 and heights[x-1][y] >= heights[x][y]:
                dfs(x-1, y, visited)
            if x < ROWS-1 and heights[x+1][y] >= heights[x][y]:
                dfs(x+1, y, visited)
            if y > 0 and heights[x][y-1] >= heights[x][y]:
                dfs(x, y-1, visited)
            if y < COLS-1 and heights[x][y+1] >= heights[x][y]:
                dfs(x, y+1, visited)

        # Left and right
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)
        # Top and bottom
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
                    
        return res


        
