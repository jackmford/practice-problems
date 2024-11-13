func calPoints(operations []string) int {
    score := []int{}

    for _, v := range operations {
        if v == "+" {
            a := score[len(score)-1]
            b := score[len(score)-2]
            tmpScore := a+b
            score = append(score, tmpScore)
        } else if v == "D" {
            a := score[len(score)-1]
            tmpScore := a*2
            score = append(score, tmpScore)
        } else if v == "C" {
            score = score[:len(score)-1]
        } else {
            n, _ := strconv.Atoi(v) 
            score = append(score, n)
        }
    }

    res := 0
    for _, v := range score {
        res = res+v
    }

    return res

