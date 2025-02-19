class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # find dupe
        s = set()
        dupe =0
        missing = 0
        for n in nums:
            if n in s:
                dupe = n
            s.add(n)

        # find number not in s
        for i in range(1, len(nums)+1):
            if i not in nums:
                missing = i
        
        return [dupe, missing]

