# greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0

        for c in s:
            if c == "(":
                leftMin+=1
                leftMax+=1
            elif c == ")":
                leftMin-=1
                leftMax-=1
            else:
                # Could be either ( )
                # ) == leftMin
                # ( == leftMax
                leftMin-=1
                leftMax+=1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return leftMin == 0
            

# dynamic programming
class Solution:
    def checkValidString(self, s: str) -> bool:

        memo = {}
        def dfs(i, open):
            if open < 0:
                return False
            
            if i == len(s):
                return open == 0
            if (i, open) in memo:
                return memo[(i, open)]

            # Three options
            if s[i] == "(":
                result = dfs(i+1, open+1)
            elif s[i] == ")":
                result = dfs(i+1, open-1)
            else:
                result = dfs(i+1, open) or dfs(i+1, open+1) or dfs(i+1, open-1)

            memo[(i, open)] = result
            return memo[(i, open)]
        return dfs(0, 0)

