"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):

            if len(arr) <= 1:
                return arr

            middle = len(arr)//2
            left = arr[:middle]
            right = arr[middle:]
            mergeSort(left)
            mergeSort(right)
            merge(arr, left, right)

            return arr
        
        def merge(arr, left, right):
            i, j, k = 0, 0, 0

            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1

            while j<len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i] = right[k]
                k+=1
                i+=1
            return arr

        return mergeSort(nums)


sol = Solution()
print(sol.sortArray([5,2,3,1]))
print(sol.sortArray([5,1,1,2,0,0]))
