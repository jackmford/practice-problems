func generateParenthesis(n int) []string {
    // Base cases
    // if open and closed == n return
    // if open < n, add open
    // if closed < n, add closed

    res := []string{}
    var r func(string, int, int)
    r = func(s string, open int, closed int) {
        if open == n && closed == n {
            res = append(res, s)
            return
        }

        if open < n {
            s += "("
            r(s, open+1, closed)
            s = s[:len(s)-1]
        }

        if closed < open {
            s += ")"
            r(s,open, closed+1)
            s = s[:len(s)-1]
        }
    }
    
    r("", 0, 0)
    return res
}
