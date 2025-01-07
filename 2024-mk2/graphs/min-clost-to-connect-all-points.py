class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Can we just djikstra here?
        # For every point calculate the distance and add it to queue?
        # If you visit, add to visited?

        q = []
        q.append((0, 0, points[0]))
        visited = set()

        total = 0
        while len(visited)!=len(points):
            cost, idx, pt = heapq.heappop(q)
            x,y = pt[0], pt[1]
            if idx in visited:
                continue

            print(cost)
            total += cost
            visited.add(idx)
            
            for i in range(len(points)):
                if points[i] != [x,y] and i not in visited:
                    dist = abs(x-points[i][0])+abs(y-points[i][1])
                    heapq.heappush(q, (dist, i, [points[i][0], points[i][1]]))
        return total
        



        
