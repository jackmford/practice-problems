class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def searchFromLocation(i, cur):
            for j in range(i, len(word)):
                print(word[j])
                if word[j] == ".":
                    # If found "." need to check all cur's children for matching char
                    for child in cur.children:
                        valid = searchFromLocation(j+1,cur.children[child])
                        if valid:
                            return True

                    # There are no more children but "." is still present, there can't possibly be a match.
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]] 
            return cur.end
            
        return searchFromLocation(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
