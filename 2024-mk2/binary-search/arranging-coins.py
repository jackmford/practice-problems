"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""

##class Solution:
##    def arrangeCoins(self, n: int) -> int:
##
##        i = 1
##        rows = 0
##        while n >= 0:
##            n = n-i
##            i+=1
##            rows += 1
##        return rows-1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l<=r:
            m = (l+r)//2
            required_coins = (m/2)*(m+1)

            if required_coins > n:
                r = m-1
            else:
                l = m+1
                res = max(m, res)

        return res

sol = Solution()
print(sol.arrangeCoins(5))
print(sol.arrangeCoins(8))
print(sol.arrangeCoins(1))
