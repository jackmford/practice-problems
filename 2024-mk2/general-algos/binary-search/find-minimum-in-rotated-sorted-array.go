func findMin(nums []int) int {
    
    l, r := 0, len(nums)-1

    var m int
    for l < r {
        m = int(l + (r-l) / 2)
        if m+1 < len(nums) && nums[m+1] < nums[m] {
            return nums[m+1]
        } else if m-1 >= 0 && nums[m-1] > nums[m] {
            return nums[m]
        } else if nums[r] > nums[m] {
            r = m-1
        } else if nums[l] < nums[m] {
            l = m+1
        }
    }
    return nums[]
}
