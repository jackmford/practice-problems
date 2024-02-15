# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
            
        
        if length % 2 == 0:
            mid = length // 2 + 1
        else:
            mid = math.ceil(length / 2)

        for i in range(mid-1):
            head = head.next
        return head