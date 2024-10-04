package main

import (
  "fmt"
)

// Binary search searches a sorted collection for a target value
func BinarySearch(arr []int, target int) int {
  left, right := 0, len(arr)-1

  for left <= right {
    mid := left + (right-left) / 2

    if arr[mid] == target {
      return target
    } else if arr[mid] < target {
      // Right half
      left = mid + 1
    } else {
      // Left Half
      right = mid - 1
    }
  }

  return -1
}

func main() {
  testArray := []int{1, 2, 3, 4, 5, 6, 11, 12, 13}
  target := 5

  fmt.Println(BinarySearch(testArray, target))
}
