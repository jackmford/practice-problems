class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = [[-1]*len(text2) for _ in range(len(text1))]
        def dfs(i, j):
            # OOB
            if i>=len(text1) or j>=len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            
            # THINK ABOUT WHAT CHOICE YOU HAVE
            moveLeft = dfs(i+1, j)
            moveRight = dfs(i, j+1)

            memo[i][j] = max(moveLeft, moveRight)
            return max(moveLeft, moveRight)


        return dfs(0, 0)

