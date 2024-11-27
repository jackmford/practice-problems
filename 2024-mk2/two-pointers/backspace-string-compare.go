func nextValid(str string, ind int) int {
    backspace := 0
    for ind >= 0 {
        if backspace == 0 && str[ind] != '#' {
            break
        } else if str[ind] == '#' {
            backspace++
            ind--
        } else {
            backspace--
            ind--
        }
    }
    return ind
}
func backspaceCompare(s string, t string) bool {
    sPtr, tPtr := len(s)-1, len(t)-1

    for sPtr >= 0 || tPtr >= 0 {
        sPtr = nextValid(s, sPtr)
        tPtr = nextValid(t, tPtr)
        var charS byte
        var charT byte
        if sPtr >= 0 {
            charS = s[sPtr]
        }
        if tPtr >= 0 {
            charT = t[tPtr]
        }
        if charS != charT {
            return false
        }
        sPtr--
        tPtr--
    }

    return true
}
