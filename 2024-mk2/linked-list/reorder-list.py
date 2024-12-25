# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle using tortoise and hare
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next # Beginning of second half new order
        slow.next = None # This will be end of first half new order
        prev = None
        # Iterate throughs econd half
        while second != None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev

        first = head
        # Reconstruct
        while second != None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head
        
