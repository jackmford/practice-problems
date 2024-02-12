# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        mid = (r+l) // 2
        while l <= r:
            nBad = isBadVersion(mid)
            lBad = isBadVersion(mid-1)
            if nBad == True and lBad == False:
                return mid
            if nBad == False:
                l = mid+1
                mid = (l+r) //2
            elif nBad == True:
                r = mid-1
                mid = (l+r) //2