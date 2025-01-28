# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        m = set()
        while curA != None:
            m.add(curA)
            curA = curA.next

        curB = headB
        while curB != None:
            if curB in m:
                return curB 
            curB = curB.next

        return None
