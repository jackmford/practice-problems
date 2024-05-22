"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i, w in enumerate(strs):
                res+= str(len(w)) + "#" + w

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        j = i
        for i in range(len(s)):
            if i < j:
                continue
            if s[i] == "#":
                length = int(s[j:i])
                x = i+1
                word = ""
                for x in range(x, x+length):
                    word+=s[x]
                res.append(word)
                j=i+1+length
        return res

