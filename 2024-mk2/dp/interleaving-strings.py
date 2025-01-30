class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # two pointers
        # if either is equal to the char at s3[i+j], move that one
        # and recurse
        # base case if both are oob
        if len(s3) != len(s1)+len(s2):
            return False
        
        memo = {}
        def dfs(i, j):
            # Both reached the end
            if i >= len(s1) and j >= len(s2) and i+j == len(s3):
                return True
            if i+j >= len(s3):
                return False
            if (i, j) in memo:
                return memo[(i, j)]

            iPtr = False
            jPtr = False 
            if i < len(s1):
                if s1[i] == s3[i+j]:
                    iPtr = dfs(i+1, j)

            if j < len(s2):
                if s2[j] == s3[i+j]:
                    jPtr = dfs(i, j+1)

            memo[(i, j)] = iPtr or jPtr
            return iPtr or jPtr

        return dfs(0,0)

