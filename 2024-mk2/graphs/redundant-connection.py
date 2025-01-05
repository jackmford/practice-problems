class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # can we BFS and if return if we find a node that is already in visited?
        # make a map of nodes and their neighbors
        def has_cycle(m, node, visited, parent):
            # We found a cycle
            if node in visited and node != parent:
                return True
            visited.add(node)
            for neighbor in m[node]:
                if has_cycle(m, neighbor, visited, node):
                    return True
            
            return False

        # Build a graph but ignore one edge each time
        # We are looking for an edge that we can leave out that still maintains a non cyclical graph
        for i in range(len(edges)):
            m = defaultdict(list)

            print(edges[:i]+edges[i+1:])
            for edge in edges[:i] + edges[i+1:]:
                print(edge)
                m[edge[0]].append(edge[1])
                m[edge[1]].append(edge[0])

            visited = set()
            if has_cycle(m, edges[0][0], visited, -1) == False:
                return edges[i]
        
        return []
