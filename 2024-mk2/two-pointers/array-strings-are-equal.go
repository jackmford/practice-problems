func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    word1Ptr, word2Ptr := 0, 0
    i, j := 0, 0

    for word1Ptr < len(word1) && word2Ptr < len(word2) {
        if word1[word1Ptr][i] != word2[word2Ptr][j] {
            return false
        }

        i++
        j++

        if i == len(word1[word1Ptr]) {
            word1Ptr++
            i = 0
        }

        if j == len(word2[word2Ptr]) {
            word2Ptr++
            j = 0
        }
    }

    if word1Ptr != len(word1) || word2Ptr != len(word2) {
        return false
    }

    return true
    
}
