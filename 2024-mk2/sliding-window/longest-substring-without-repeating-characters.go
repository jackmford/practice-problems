func lengthOfLongestSubstring(s string) int {
    // maintain a map
    // start both positions at 0
    // add right item
    // if it is present already, move left pointer and remove item
    m := map[byte]int{}
    left,right := 0,0
    res := 0

    for right < len(s) {
        // Check if right char is already in the substring
        _, ok := m[s[right]]
        // If char is already in substring
        if ok {
            delete(m, s[left])
            left++
        } else {
            m[s[right]]++
            right++
        }

        if len(m) > res {
            res = len(m)
        }

    }

    return res
    
}
