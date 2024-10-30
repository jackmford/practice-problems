package main

import "fmt"

type DataPt struct {
  buy int;
  sell int;
  profit int;
}

func maxProfit(prices []int, dp *DataPt) int {
  l, r := 0, 1

  for r < len(prices) {
    if prices[r] < prices[l] {
      l = r
      r++
      continue
    }
    tmp := prices[r] - prices[l]
    if tmp > dp.profit {
      dp.profit = tmp
      dp.buy = l
      dp.sell = r
    }
    r++
  }
  fmt.Println(dp.buy)
  fmt.Println(dp.sell)

  return dp.profit
}

func main() {
  dp := &DataPt{0, 1, 0}
  prices := []int{7, 1, 5, 3, 6, 4}
  fmt.Println(maxProfit(prices, dp))

  dp = &DataPt{0, 1, 0}
  prices2 := []int{7, 6, 4, 3, 1}
  fmt.Println(maxProfit(prices2, dp))

}
