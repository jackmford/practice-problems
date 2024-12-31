def isPalindrome(word):
    i, j = 0, len(word)-1
    while i<=j:
        if word[i]!=word[j]:
            return False
        i+=1
        j-=1
    return True
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # All parts of the string must be present in the partition

        res = []
        currentPart = []
        def dfs(currentIdx):
            # Base case is our idx reached end of s
            if currentIdx == len(s):
                # Copy
                res.append(currentPart[:])
                return
            
            for end in range(currentIdx, len(s)):
                print(s[currentIdx:end+1], isPalindrome(s[currentIdx:end+1]))
                if isPalindrome(s[currentIdx:end+1]):
                    currentPart.append(s[currentIdx:end+1])
                    dfs(end+1)
                    currentPart.pop()
        dfs(0)
        return res
