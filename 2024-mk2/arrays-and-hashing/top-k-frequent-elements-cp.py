"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        sorted_counts = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}
        res = []
        for key in sorted_counts:
            res.append(key)
            if len(res) == k:
                return res


sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))

