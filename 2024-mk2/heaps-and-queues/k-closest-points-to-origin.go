 func kClosest(points [][]int, k int) [][]int {
    // For every point, calculate the distance
    // Store the distances in some sort of sortable data structure
    // We are using a minHeap here by using a priority queue that prioritizes smallest values being at the front. This way we can just iterate through k times and put them in the res.
    // Return the first K points
    
    // Create a maxHeap implementation with a priorityqueue
    maxHeap := priorityqueue.NewWith(func(a, b interface{}) int {
        distA := a.([]int)[2]
        distB := b.([]int)[2]
        if distA > distB {
            return 1
        } else if distA < distB {
            return -1
        }
        return 0
    })

    for _, p := range points {
        dist := p[0]*p[0] + p[1]*p[1]
        maxHeap.Enqueue([]int{p[0], p[1], dist})
    }
    
    res := [][]int{}
    for i:=0; i<k; i++ {
        val, _ := maxHeap.Dequeue()
        point := val.([]int)
        res = append(res, []int{point[0], point[1]})
    }


    return res
    
}
