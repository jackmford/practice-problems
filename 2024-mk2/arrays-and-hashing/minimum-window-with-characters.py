"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        # if you find the substring containing characters
        # you could move the left and right ptrs to the 2nd occurence?
        l, r = 0,0
        in_out = [0] * len(t)
        print(in_out)
        while r < len(s):
            for i in range(len(t)):
                if t[i] in s[l:r] and in_out[i] == 0:
                    r+=1
                    in_out[i] = i
            # found all chars
            if 0 not in in_out:
                in_out = sorted(in_out)[1]
        return res

sol = Solution()
sol.minWindow("OUZODYXAZV", "XYZ")

