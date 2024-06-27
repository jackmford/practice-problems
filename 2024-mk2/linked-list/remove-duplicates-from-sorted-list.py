"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        while head != None:
            if tail.val == head.val:
                tail.next = head.next
                head = tail.next
            else:
                tail = tail.next
                head = head.next
        return dummy.next
