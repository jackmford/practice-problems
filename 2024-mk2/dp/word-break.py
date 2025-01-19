class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        found = False
        memo = {len(s): True}
        def dfs(i, word):
            nonlocal found
            if i in memo:
                return memo[i]
            if i == len(s):
                return True

            for w in wordDict:
                # Choose
                if i+len(w) <= len(s):
                # If position in word == word we're checking
                    if s[i:i+len(w)] == w:
                        if dfs(i+len(w), word+w):
                            memo[i] = True
                            return True
                            
            memo[i] = False 
            return False
        
        return dfs(0, "")

        
