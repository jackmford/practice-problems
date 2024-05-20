"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for n in nums:
            d[n]+=1

        sorted_dict = [k for k, _ in sorted(d.items(), key=lambda item: item[1], reverse=True)]

        return sorted_dict[:k]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
