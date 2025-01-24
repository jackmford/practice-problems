# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = {}
        cur = head

        while cur != None:
            if cur in m:
                return True
            m[cur] = True
            cur = cur.next

        return False
        
        #fast, slow = head, head
#
        #while fast != None and fast.next != None:
        #    fast = fast.next.next
        #    slow = slow.next
        #    if fast == slow:
        #        return True
#
        #return False

