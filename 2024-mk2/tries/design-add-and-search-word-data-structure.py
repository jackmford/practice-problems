class TrieNode:
    def __init__(self):
        self.m = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.m:
                cur.m[char] = TrieNode()
            cur = cur.m[char]
        
        cur.end = True

    def search(self, word: str) -> bool:

        # This function searches from any index for validity
        def searchRemainder(cur, i):
            for j in range(i, len(word)):
                if word[j] == ".":
                    # For every option in cur ("." == any character)
                    for c in cur.m:
                        if searchRemainder(cur.m[c], j+1):
                            return True
                    # There are no more characters to check, found no valid word
                    return False
                if word[j] in cur.m:
                    cur = cur.m[word[j]]
                else:
                    return False
            return cur.end

        return searchRemainder(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
