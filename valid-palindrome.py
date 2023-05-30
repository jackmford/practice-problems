import re


class Solution:
    # Sol 1
    #def isPalindrome(self, s: str) -> bool:
    #    s = re.sub(r"[^a-zA-Z0-9]", "", s)
    #    s = s.lower()
    #    print(s)
    #    reverseString = ""
    #    for i in range(len(s)-1, -1, -1):
    #        reverseString += s[i]
    #    if s == reverseString:
    #        return True
    #    return False

    # Sol 2
    def isPalindrome(self, s: str) -> bool:

sol = Solution()
print(sol.isPalindrome('Race: car'))