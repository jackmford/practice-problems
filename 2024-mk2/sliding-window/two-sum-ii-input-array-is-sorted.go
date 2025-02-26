func twoSum(numbers []int, target int) []int {
    // Two ptrs, one at start one at end
    // If the sum is too large, move right ptr
    // If the sum is too small, move left ptr
    // Keep going until they cross
    left, right := 0, len(numbers)-1
    res := []int{}

    for left < right {
        if numbers[left] + numbers[right] == target {
            res = append(res, left+1)
            res = append(res, right+1)
            break
        } else if numbers[left] + numbers[right] > target {
            right--
        } else {
            left++
        }
    }
    return res
}
