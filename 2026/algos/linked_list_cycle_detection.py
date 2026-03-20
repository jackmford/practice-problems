# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        # two ptrs will eventually be the same
        slow, fast = head, head.next

        while slow != None and fast != None:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                break

        return False
