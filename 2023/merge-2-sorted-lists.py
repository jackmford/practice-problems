from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
            
        

sol = Solution()
thr = ListNode(4)
t = ListNode(2, thr)
o = ListNode(1, t)

thr2 = ListNode(4)
t2 = ListNode(3, thr2)
o2 = ListNode(1, t2)
print(sol.mergeTwoLists(o, o2).val)
