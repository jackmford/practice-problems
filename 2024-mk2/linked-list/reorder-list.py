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
        # Split the list in half
        # Set last item in first half to the new end
        # Need to switch pointers around in the back half
        # Then start to recreate the linked list

        # Find halfway
        fast, slow = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        lastHalf = slow.next
        slow.next = None
        prev = None
        while lastHalf != None:
            # Save where we currently are
            tmp = lastHalf
            # Move to next item
            lastHalf = lastHalf.next
            # Set where we were to the previous element to reverse order
            tmp.next = prev
            # Prev becomes where we were
            prev = tmp

        # Start joining things
        # Cur is start, prev is last item in list
        cur = head
        end = prev
        # End will be shorter of two
        while end != None:
            # Save the next pointers
            curNext, endNext = cur.next, end.next
            # Set current pointer to end item
            # 1 -> 2 becomes 1 -> 5
            cur.next = end
            # Set end pointer to old item's next
            # So 1 -> 2 becomes 1 -> 5 -> 2
            end.next = curNext
            # Move both pointers to their saved next's
            # 1 becomes 2 and 5 becomes 4 for example,  skipping over any items that were added.
            cur = curNext
            end = endNext
        
