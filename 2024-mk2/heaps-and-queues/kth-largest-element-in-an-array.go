func findKthLargest(nums []int, k int) int {
    maxHeap := priorityqueue.NewWith(func(a, b interface{}) int {
        intA := a.(int)
        intB := b.(int)
        if intA > intB {
            return -1
        } else if intA < intB {
            return 1
        }
        return 0
    })

    for _, n := range nums {
        maxHeap.Enqueue(n)
    }
    for i:=0; i<=k-1; i++ {
        val, _ := maxHeap.Dequeue()
        if i == k-1 {
            return val.(int)
        }
    }
    return 0
}

