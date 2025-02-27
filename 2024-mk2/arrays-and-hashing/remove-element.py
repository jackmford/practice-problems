class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # probe for numbers != val
        # keep a pointer at the head of the nums array
        # move any nums != val to the head
        one = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[one] = nums[i]
                one+=1
        return one

