class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        h = []
        for n in nums:
            d[n] += 1
        for key, val in d.items():
            heapq.heappush(h, (val, key))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for i in range(k):
            num = heapq.heappop(h)
            res.append(num[1])
        return res
