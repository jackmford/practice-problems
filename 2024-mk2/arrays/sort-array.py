"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # MergeSort

        def merge(arr, leftArray, rightArray):
            i, j, k = 0, 0, 0

            while j<len(leftArray) and k<len(rightArray):
                if leftArray[j] <= rightArray[k]:
                    arr[i] = leftArray[j]
                    j += 1
                else:
                    arr[i] = rightArray[k]
                    k+=1
                i+=1

            while j<len(leftArray):
                arr[i] = leftArray[j]
                j += 1
                i += 1
            while k<len(rightArray):
                arr[i] = rightArray[k]
                k += 1
                i += 1
            return arr

        def mergeSort(arr):
            if len(arr)<=1:
                return arr

            m = len(arr)//2
            # You must make copies
            left = arr[:m]
            right = arr[m:]
            mergeSort(left)
            mergeSort(right)
            merge(arr, left, right)

            return arr

        return mergeSort(nums)

sol = Solution()
print(sol.sortArray([5,2,3,1]))
print(sol.sortArray([5,1,1,2,0,0]))
