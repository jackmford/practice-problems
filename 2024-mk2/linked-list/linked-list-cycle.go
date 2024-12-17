* Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    // Brute force approach
    tmpHead := head
    l := []*ListNode{}
    // Create an array of ListNodes
    for head != nil {
        l = append(l, head)
        head = head.Next
    }
    // Calculate item to remove
    remove := len(l)-n
    // If the element is the first in the array, remove the Next (will be nil if it is alone)
    if remove == 0 {
        return tmpHead.Next
    }
    // Find the element BEFORE the element to remove, and set it's next to the item to remove's next
    l[remove-1].Next = l[remove].Next

    
    return tmpHead
}
