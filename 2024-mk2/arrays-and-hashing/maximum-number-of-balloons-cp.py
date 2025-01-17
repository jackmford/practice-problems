"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < len("balloon"):
            return 0
        d = defaultdict(int)
        for c in text:
            d[c] += 1
        res = float("INF")
        for c in "balloon":
            if c == "l" or c == "o":
                res = min(d[c]//2, res)
            else:
                res = min(d[c], res)
        return int(res)




sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))
print(sol.maxNumberOfBalloons("balon"))
