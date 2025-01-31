class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # If both pointers are equal you can move them both
        # If they are not, m
        # Insert = dfs(i, j+1)
        # Delete = dfs(i+1, j)
        # Replace = dfs(i+1, j+1)
        memo = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            if (i,j) in memo:
                return memo[(i,j)]
            
            insert = dfs(i, j+1)
            delete = dfs(i+1, j)
            replace = dfs(i+1, j+1)

            memo[(i,j)] = 1+min(insert,delete,replace)
            return memo[(i,j)]

        return dfs(0,0)
