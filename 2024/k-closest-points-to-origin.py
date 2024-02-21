class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x*x) + (y*y)
            heap.append([dist, x, y])

        heapq.heapify(heap)
        res = []        
        # Find closest K points
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
    
        return res