func findDuplicate(nums []int) int {

    // Mark values at the current values corresponding index negative
    // If you look at one and it is already negative, return abs value of it.

    for _, num := range nums {
        if nums[abs(num)-1] < 0 {
            return abs(num)
        }
        nums[abs(num)-1] = nums[abs(num)-1]*-1
    }
    return 0
}

func abs(a int) int {
    if a >= 0 {
        return a
    } else {
        return a*-1
    }
}
