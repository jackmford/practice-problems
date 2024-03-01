"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return
        m, visited = {}, set()
        q = []
        q.append(node)
        while q:
            cur = q.pop(0)
            if cur not in visited:
                copy = Node(cur.val)
                if cur not in m:
                    m[cur] = copy
                for neighb in cur.neighbors:
                    neiCopy = Node(neighb.val)
                    if neighb not in m:
                        m[neighb] = neiCopy
                    m[cur].neighbors.append(m[neighb])
                    q.append(neighb)
                
                visited.add(cur)
        return m[node]
