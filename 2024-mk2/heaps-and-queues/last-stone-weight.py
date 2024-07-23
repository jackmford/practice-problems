"""
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.
"""
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.minHeap = [-s for s in stones]
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > 1:
            print(self.minHeap)
            y = heapq.heappop(self.minHeap)
            x = heapq.heappop(self.minHeap)
            if x > y:
                heapq.heappush(self.minHeap, (y-x))
        print(self.minHeap)
        if len(self.minHeap)>0:
            return abs(self.minHeap[0])
        return 0

