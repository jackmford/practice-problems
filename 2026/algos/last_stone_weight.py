class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heap = stones
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -abs(y - x))

        if len(heap) == 0:
            return 0
        return abs(heapq.heappop(heap))
