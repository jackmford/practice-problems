class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        l, r = 0, 0
        total = 0
        nums = sorted(nums)
        print(nums)

        while r < len(nums):
            total+=nums[r]

            # Is window valid?
            # If not, shrink it
            # If window is valid record window size and move the right pointer
            # Always want to check right away if the last addition of the right pointer made window invalid
            # instead of just adding right away and then recording
            while ((nums[r]*(r-l+1)) - total) > k:
                total-=nums[l]
                l+=1

            # Once we have a valid window, record window size and move the right pointer
            res = max(r-l+1, res)
            r+=1


        return res
        
