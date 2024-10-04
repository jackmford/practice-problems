package main

func searchInsert(nums []int, target int) int {
  left, right := 0, len(nums)-1
  var middle int

  for left <= right {
    middle = left + (right - left) / 2
    
    if nums[middle] == target {
      return middle
    } else if nums[middle] < target {
      left = middle + 1
    } else {
      right = middle - 1
    }
  }
  if target > nums[middle] {
    return middle+1
  } else {
    return left
  }
}
