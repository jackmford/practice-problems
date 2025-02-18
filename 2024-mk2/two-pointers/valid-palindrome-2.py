"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            if s[l] != s[r]:
                if s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]:
                    return True
                else:
                    return False
            else:
                l+=1
                r-=1

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
