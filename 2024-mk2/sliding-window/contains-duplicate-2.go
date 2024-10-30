package main

import "fmt"

func containsNearbyDuplicate(nums []int, k int) bool {
  // Initialize window, window size must be <= k
  left, right := 0, 0
  keepTrack := map[int]bool{}

  // Iterate through windows checking condition
  for right < len(nums) {
    if _, ok := keepTrack[nums[right]]; ok {
      return true
    }

    keepTrack[nums[right]] = true

    if len(keepTrack) > k {
      delete(keepTrack, nums[left])
      left++
    }
    right++
  }
  return false
}

func main() {
  nums := []int{1,2,3,1}
  k := 3

  fmt.Println(containsNearbyDuplicate(nums, k))

  nums = []int{1,2,3,1,2,3}
  k = 2
  fmt.Println(containsNearbyDuplicate(nums, k))

  nums = []int{1,2,1}
  k = 0
  fmt.Println(containsNearbyDuplicate(nums, k))
}
