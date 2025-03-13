class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                # w1 is longer than w2
                if j == len(w2):
                    return False 

                if w1[j] != w2[j]:
                    # char at this pos is > in w1 than w2
                    if order[w1[j]] > order[w2[j]]:
                        return False
                    break

            return True
        
