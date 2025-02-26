func minSubArrayLen(target int, nums []int) int {
    left, right := 0, 0
    res := len(nums)+1
    total := 0
    found := false
    
    for right < len(nums) {
        total = total+nums[right]
        for total >= target {
            if right-left+1 < res {
                res = right-left+1
                found = true
            }
            total = total-nums[left]
            left++
        }
        right++
    }
    if found {
        return res
    }
    return 0
}
