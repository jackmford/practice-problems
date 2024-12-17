/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    // Find middle of the list using tortoise and hare
    begin, end := head, head.Next
    for end != nil && end.Next != nil {
        begin = begin.Next
        end = end.Next.Next
    }

    // Reverse the second half of the list
    second := begin.Next
    begin.Next = nil
    var prev *ListNode
    for second != nil {
        tmp := second.Next
        second.Next = prev
        prev = second
        second = tmp
    }

    // Merge the first and second halves
    first := head
    second = prev
    for second != nil {
        tmp1, tmp2 := first.Next, second.Next
        first.Next = second
        second.Next = tmp1
        first = tmp1
        second = tmp2
    }
}

