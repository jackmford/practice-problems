package main

import "fmt"

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
  arr := []int{1, 2, 5, 33, 222, 1000, 10001}
  target := 100023

  fmt.Println(BinarySearch(arr, target))
  
}
