"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""
from typing import List
from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_counts = defaultdict(int)
        for c in chars:
            char_counts[c] += 1

        for word in words:
            d = defaultdict(int)
            for char in word:
                d[char] +=1

            
            ct = 0
            for k,v in d.items():
                if k not in char_counts or d[k] > char_counts[k]:
                    ct = 0
                    break
                if d[k] <= char_counts[k]:
                    ct += v
            res+=ct
        return res




sol = Solution()
print(sol.countCharacters(["cat","bt","hat","tree"], "atach"))
