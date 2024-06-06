"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = 0
        l,r = 0, len(s)-1

        while l<=r: 
            if s[l] != s[r]:
                if s[l+1:r+1] == s[l+1:r+1][::-1]:
                    l+=1
                else:
                    r-=1
                delete += 1
            else:
                l += 1
                r -= 1
            if delete > 1:
                return False

        return True


        
sol = Solution()
print(sol.validPalindrome("cbbcc"))
print(sol.validPalindrome("aba"))
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("abc"))
print(sol.validPalindrome("abcca"))
print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
