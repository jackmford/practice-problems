func compareDict(s1Map, s2Map map[byte]int) bool {
    for key, value := range s1Map {
        if v, exists := s2Map[key]; !exists || v != value {
            return false
        }
    }
    return true
}
func checkInclusion(s1 string, s2 string) bool {
    // Is this the same as the anagrams, but easier?
    // Create map of s2 letters
    // Create map of s1 letters
    // Compare the two, if they are equal, return,
    // Else, start the window comparisons
    if len(s1) > len(s2) {
        return false
    }

    s1Map := map[byte]int{}
    s2Map := map[byte]int{}

    for i, _ := range s1 {
        s1Map[s1[i]]++
        s2Map[s2[i]]++
    }

    left, right := 0, len(s1)
    if compareDict(s1Map, s2Map) {
        return true
    }

    for right < len(s2) {
        s2Map[s2[left]]--
        s2Map[s2[right]]++
        left++
        right++
        if compareDict(s1Map, s2Map) {
            return true
        }
    }
    return false
}
