package main

import (
  "fmt"
)

func calculate(s byte) int{
  if s == 'I' {
    return 1
  }
  if s == 'V' {
    return 5
  }
  if s == 'X' {
    return 10
  }
  if s == 'L' {
    return 50
  }
  if s == 'C' {
    return 100
  }
  if s == 'D' {
    return 500
  }
  if s == 'M' {
    return 1000
  }
  return 0
}

func romanToInt(s string) int {
  total := 0
  for i := 0; i < len(s); i++ {
    tmp := 0
    if i != len(s)-1 {
      tmp = calculate(s[i])
      if s[i] == 'I' && s[i+1] == 'V' {
        total += 4
        i += 1
        continue
      }
      if s[i] == 'I' && s[i+1] == 'X' {
        total += 9
        i += 1
        continue
      }
      if s[i] == 'X' && s[i+1] == 'L' {
        total += 40
        i += 1
        continue
      }
      if s[i] == 'X' && s[i+1] == 'C' {
        total += 90
        i += 1
        continue
      }
      if s[i] == 'C' && s[i+1] == 'D' {
        total += 400
        i += 1
        continue
      }
      if s[i] == 'C' && s[i+1] == 'M' {
        total += 900
        i += 1
        continue
      }
      fmt.Println("adding + %s", tmp)
      total += tmp
    } else {
        total += calculate(s[len(s)-1])
    }
  }
  return total
}

func main() {
  final := romanToInt("IV")
  fmt.Println(final)
}
