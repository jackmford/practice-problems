"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""
from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            i, j = 0, len(word)-1
            while i<j:
                if word[i] != word[j]:
                    break
                i+=1
                j-=1
            if i >= j:
                return word
        return ""
            
                

sol = Solution()
print(sol.firstPalindrome(["abc","car","ada","racecar","cool"]))
