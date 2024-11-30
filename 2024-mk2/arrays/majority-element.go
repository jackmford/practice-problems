func majorityElement(nums []int) int {
    res, count := 0, 0

    for _, v := range nums {
        if count == 0 {
            res = v
            count++
        } else if v != res {
            count--
        } else {
            count++
        }
    }

    return res
    
}
