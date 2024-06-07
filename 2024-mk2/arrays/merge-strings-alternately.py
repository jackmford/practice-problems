"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        len1 = len(word1)
        len2 = len(word2)
        res = ""

        while i<len1 and j<len2:
            if i <= j:
                res += word1[i]
                i+=1
            else:
                res += word2[j]
                j+=1

        while i<len1:
            res += word1[i]
            i+=1
        while j<len2:
            res += word2[j]
            j+=1

        return res


sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
print(sol.mergeAlternately("ab", "pqrs"))
        
