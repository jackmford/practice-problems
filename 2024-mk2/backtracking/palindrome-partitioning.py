class Solution:
    def isPalindrome(self, word):
        i = 0
        j = len(word)-1
        while i < j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partition = []

        def dfs(start):
            nonlocal partition
            # If i == len S we checked all combos for that character
            if start >= len(s):
                res.append(partition[:])
                return


            # If there is a substring, check next character
            for end in range(start, len(s)):
                # Second number (j) is not inclusive
                print(start, end)
                slicey = s[start:end+1]
                if self.isPalindrome(slicey):
                    partition.append(slicey)
                    dfs(end+1)
                    partition.pop()


            
        dfs(0)
        return res 

