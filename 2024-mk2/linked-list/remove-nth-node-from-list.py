# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        cur = head
        while cur != None:
            sz += 1
            cur = cur.next
        idx = sz - n
        if idx == 0:
            return head.next

        ctr = 0
        cur = head
        while cur != None:
            if ctr+1 == idx:
                cur.next = cur.next.next
                break
            cur = cur.next 
            ctr+=1
        print(idx)
        return head
        
