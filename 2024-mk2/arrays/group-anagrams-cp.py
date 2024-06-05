"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            d[sort].append(i)
        for _,v in d.items():
            tmp = []
            for index in v:
                tmp.append(strs[index])
            res.append(tmp)
        return res

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

