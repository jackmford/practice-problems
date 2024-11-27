func findContentChildren(g []int, s []int) int {
    
    cookies, kids := 0, 0
    sort.Ints(g)
    sort.Ints(s)
    res := 0
    fmt.Println(g, s)

    for cookies < len(s) && kids < len(g) {
        if s[cookies] >= g[kids] {
            res++
            cookies++
            kids++
        } else {
            cookies++
        }
    }
    
    return res
    

