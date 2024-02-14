# Attempt 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        res, maxCount = 0, 0
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            if m[n] > maxCount:
                res = n
        
        return res

# Attempt 2 Boyer-Moore Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
                count += 1
            elif n != res:
                count -= 1
            else:
                count += 1
        return res
            
        