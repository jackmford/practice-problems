class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # For every character, create a TrieNode, add it to root's children
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            # From where we are to the end of the word check if it is valid
            # I is where we're starting, J is where we are
            for j in range(i, len(word)):
                c = word[j]
                print(c)
                # If we encounter a "."
                if c == ".":
                    # Pass every child trienode into function to try for validity
                    for child in cur.children.values():
                        # Move past the "." and check validation on child
                        # Call from where we are onward (using I here is where we started)
                        valid = dfs(j+1, child)
                        if valid:
                            return True
                    # Not valid after "."
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)

