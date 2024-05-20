"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
"""
res = defaultdict(list)

        for s in strs:
            chars = [0]*26
            for char in s:
                chars[ord(char) - ord('a')] += 1
            res[tuple(chars)].append(s)
        return res.values()
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        res = []

        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            d[sort].append(i)
        for k,v in d.items():
            tmp = []
            for i in v:
                tmp.append(strs[i])

            res.append(tmp)
        return res

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

