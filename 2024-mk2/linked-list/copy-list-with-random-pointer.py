"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        cur = head
        idx = 0
        if head is None:
            return None

        while cur != None:
            copies[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur != None:
            cp = copies[cur]

            if cur.next == None:
                cp.next = None
            else:
                cp.next = copies[cur.next]

            if cur.random == None:
                cp.random = None
            else:
                cp.random = copies[cur.random]

            cur = cur.next

        return copies[head]
        
