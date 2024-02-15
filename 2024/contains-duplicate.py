class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for n in nums:
            if n in nums:
                return False
            else:
                nums[n] = 0
        
        return True