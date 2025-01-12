class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, maxLen):
            if i >= maxLen:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            # Skip
            left = dfs(i+1, maxLen)
            # Rob
            right = nums[i] + dfs(i+2, maxLen)

            memo[i] = max(left, right)

            return max(left, right)
        
        # If there is only one house
        if len(nums) == 1:
            return nums[0]

        # Start from first house, don't include last house
        memo = [-1] * len(nums)
        firstHouse = dfs(0, len(nums)-1)

        # Start from second house, include last house
        memo = [-1] * len(nums)
        secondHouse = dfs(1, len(nums))
        return max(firstHouse, secondHouse)
