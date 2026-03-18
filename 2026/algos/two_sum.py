class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        x, y = 0, 0

        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                x = nums_dict[target - nums[i]]
                y = i
            nums_dict[nums[i]] = i
        return [x, y]
