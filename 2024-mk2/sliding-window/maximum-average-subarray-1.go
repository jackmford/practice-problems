package main

import "fmt"

func findMaxAverage(nums []int, k int) float64 {
  // Keep track of sum and divide by k for avg
  sum := 0
  // Process first window 
  for i, _ := range nums[0:k] {
    sum += nums[i]
  }
  // Initialize maximum average
  maxAvg := float64(sum) / float64(k)

  // Initialize left and right pointers
  left, right := 1, k
  for right < len(nums) {
    sum = (sum - nums[left-1] + nums[right])
    if (float64(sum) / float64(k)) > maxAvg {
      maxAvg = float64(sum) / float64(k)
    }
    left++
    right++
  }

  return maxAvg

}

func main() {
  k := 4
  nums := []int{1,12,-5,-6,50,3}
  fmt.Println(findMaxAverage(nums, k))

  k = 1
  nums = []int{5}
  fmt.Println(findMaxAverage(nums, k))
}
