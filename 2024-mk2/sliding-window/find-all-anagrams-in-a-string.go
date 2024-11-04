package main

import (
  "fmt"
)

func compareUnorderedSlices(slice1, slice2 map[byte]int) bool {
    for key, value := range slice2 {
      if v, exists := slice1[key]; !exists || v != value {
        return false
      }
    }

    return true
}

func findAnagrams(s string, p string) []int {
  pMap := map[byte]int{}
  res := []int{}

  for i, _ := range p {
    pMap[p[i]]++
  }

  sMap := map[byte]int{}
  if len(p) > len(s) {
    return res
  }
  for i, _ := range s[0:len(p)] {
    sMap[s[i]]++
  }

  if compareUnorderedSlices(sMap, pMap){
    res = append(res, 0)
  }
  l, r := 0, len(p)
  for r < len(s) {
    fmt.Println(sMap, pMap)
    sMap[s[l]]--
    sMap[s[r]]++
    l++
    r++
    if compareUnorderedSlices(sMap, pMap){
      res = append(res, l)
    }
  }

  return res
}

func main() {
  s := "cbaebabacd"
  p := "abc"
  fmt.Println(findAnagrams(s, p))

  s = "baa"
  p = "aa"
  fmt.Println(findAnagrams(s, p))

}
