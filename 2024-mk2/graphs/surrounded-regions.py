class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # For every O on an edge, mark it as 1 and do the same for all of its neighbors
        def dfs(x,y):

            board[x][y] = "1"


            if x > 0:
                if board[x-1][y] == "O":
                    dfs(x-1, y)
            if x < ROWS-1:
                if board[x+1][y] == "O":
                    dfs(x+1, y)
            if y > 0:
                if board[x][y-1] == "O":
                    dfs(x, y-1)
            if y < COLS-1:
                if board[x][y+1] == "O":
                    dfs(x, y+1)




        # Identify O on the edge to mark as "not surroundable"
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        # Mark all of the remaining Os as surrounded and any 1s back to Os
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "1":
                    board[r][c] = "O"
