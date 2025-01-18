class Solution:
    def numDecodings(self, s: str) -> int:
       
        memo = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            one = dfs(i+1)

            if i < len(s)-1 and (s[i] == '1' or (s[i]== '2' and s[i+1] < '7')):
                one += dfs(i+2)

            memo[i] = one
            
            return one

        return dfs(0)

       
