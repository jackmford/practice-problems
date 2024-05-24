"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]

        for i in range(1, numRows):
            curRow = [1]

            for j in range(1, i):
                curRow.append(res[i-1][j-1]+res[i-1][j])

            curRow.append(1)

            res.append(curRow)

        return res

sol = Solution()
print(sol.generate(5))

