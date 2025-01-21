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

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = [[-1]*len(text2) for _ in range(len(text1))]
        def dfs(i, j):
            # OOB
            if i>=len(text1) or j>=len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            
            # THINK ABOUT WHAT CHOICE YOU HAVE
            moveLeft = dfs(i+1, j)
            moveRight = dfs(i, j+1)

            memo[i][j] = max(moveLeft, moveRight)
            return max(moveLeft, moveRight)


        return dfs(0, 0)

