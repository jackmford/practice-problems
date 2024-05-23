"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max is -1, base case
        # go through in reverse order
        # setting arr[i] to the max of rightMax
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            tmpMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = tmpMax
        return arr 

sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))

