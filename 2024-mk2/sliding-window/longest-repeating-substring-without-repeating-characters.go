package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
  l, r := 0, 0
  set := make(map[byte]bool)
  maxLen := 0

  for r < len(s) {
    if !set[s[r]] {
      set[s[r]] = true
      r++
    } else {
      delete(set, s[l])
      l++
    }
    if len(set) > maxLen {
      maxLen = len(set)
    }
  }
  return maxLen
}

func main() {
  fmt.Println(lengthOfLongestSubstring("abcabcbb"))
  fmt.Println(lengthOfLongestSubstring("bbbb"))
  fmt.Println(lengthOfLongestSubstring("pwwkew"))
}
