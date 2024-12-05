func maxSubArray(nums []int) int {
    curMax := nums[0]
    max := nums[0]

    for i:=1; i<len(nums); i++ {
        if curMax+nums[i] > nums[i] {
            curMax = curMax+nums[i]
        } else {
            curMax = nums[i]
        }
        if curMax > max {
            max = curMax
        }
    }
    return max
}
