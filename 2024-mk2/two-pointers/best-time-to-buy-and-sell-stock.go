package main

import "fmt"

func maxProfit(prices []int) int {
  // Initialize left and right pointers 
  left, right := 0, 1

  // Initialize maxProfit
  maxProfit := 0

  // Go through the prices array
  for right < len(prices) {
    // If the right pointer value is less than left, move left to right to buy on that day
    if prices[right] < prices[left] {
      left = right
      right++
      continue
    }

    // Continue moving right pointer and testing for max profit
    tmpProfit := prices[right] - prices[left]
    if tmpProfit > maxProfit {
      maxProfit = tmpProfit
    }

    right++
  }

  return maxProfit
}

func main() {
  prices := []int{7, 1, 5, 3, 6, 4}
  prices2 := []int{7, 6, 4, 3, 1}

  fmt.Println(maxProfit(prices))
  fmt.Println(maxProfit(prices2))

}
