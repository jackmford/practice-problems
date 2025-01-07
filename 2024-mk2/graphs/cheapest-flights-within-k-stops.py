class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = defaultdict(list)
        for sr, dist, price in flights:
            m[sr].append((dist,price))

        q = [(0, 0, src)]
        print(src)
        prices = [float("inf")]*n
        prices[src] = 0

        while q:
            stops, price, city = heapq.heappop(q)
            
            # Going anywhere from here is too many stops
            if stops > k:
                continue
            
            # For neighbors that are "in range", record a lower price if there is one
            for neighbor, price2 in m[city]:
                if price+price2 < prices[neighbor]:
                    print(neighbor, price2)
                    prices[neighbor] = price+price2
                    heapq.heappush(q, (stops+1, price2+price, neighbor))

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]
        
