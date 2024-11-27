func backspaceCompare(s string, t string) bool {
   stackS := []rune{}
   stackT := []rune{} 

   for _, v := range s {
    if v != '#' {
        stackS = append(stackS, v)
    } else {
        if len(stackS) > 0 {
            stackS = stackS[:len(stackS)-1]
        }
    }
   }
   for _, v := range t {
    if v != '#' {
        stackT = append(stackT, v)
    } else {
        if len(stackT) > 0 {
            stackT = stackT[:len(stackT)-1]

        }
    }
   }

    if len(stackS) != len(stackT) {
        return false
    }
    for i, _ := range(stackS) {
        if stackS[i] != stackT[i] {
            return false
        }
    }

   return true

