func makeGood(s string) string {
    stack := []string{}
    for _, v := range s {
        if len(stack) > 0 && stack[len(stack)-1] != string(v) && strings.ToLower(stack[len(stack)-1]) == strings.ToLower(string(v)) {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, string(v))
        }
    }

    return strings.Join(stack,"")

