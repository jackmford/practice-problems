# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        # go through linked list
        while head != None:
            tmp = head
            next = head.next
            head.next = prev
            head = next
            prev = tmp

        return prev
