class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # at any character you can do three things
        # i.e. three choices per location
        #
        memo = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            ins = dfs(i, j + 1)
            delet = dfs(i + 1, j)
            res = min(ins, delet)
            res = min(res, dfs(i + 1, j + 1))
            memo[(i, j)] = res + 1
            return res + 1

        return dfs(0, 0)
