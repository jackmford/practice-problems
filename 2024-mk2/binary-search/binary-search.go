package main

import (
  "fmt"
)

func BinarySearch(arr []int, target int) int {
  left, right := 0, len(arr)-1

  for left <= right {
    middle := left + (right - left) / 2

    if arr[middle] == target {
      return middle
    } else if arr[middle] < target {
      left = middle + 1
    } else {
      right = middle - 1
    }
  }
  return -1
}

func main() {
  arr := []int{1, 2, 5, 6, 11, 13, 1333, 1315, 15555}

  target := 1 
  fmt.Println(BinarySearch(arr, target))
}
