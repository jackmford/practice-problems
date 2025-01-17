"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        t = [[1]]

        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(t[i-1][j-1]+t[i-1][j])
            row.append(1)
            t.append(row)
            if i == rowIndex:
                return row




sol = Solution()
print(sol.getRow(3))
