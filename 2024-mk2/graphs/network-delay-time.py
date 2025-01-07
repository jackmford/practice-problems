class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Shortest path to any node
        # Use Djikstra BFS with minheap
        m = defaultdict(list)
        for time in times:
            m[time[0]].append([time[2], time[1]])

        q = [(0, k)]
        visited = set()
        pathTime = 0

        while q:
            time, node = heapq.heappop(q)
            if node in visited:
                continue

            # The time taken to get here
            pathTime = time
            visited.add(node)

            for time2, node2 in m[node]:
                if node2 not in visited:
                    heapq.heappush(q, (time2+pathTime, node2))
            
        # If len(visited) we have visited n nodes
        return pathTime if len(visited) == n else -1

        
