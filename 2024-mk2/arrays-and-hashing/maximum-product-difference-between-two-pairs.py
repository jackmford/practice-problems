class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # We want the two largest and two smallest numbers
        # One pass method, finding largest and smallest two nums
        # if n is greater or smaller than current largest or smallest, set 2nd largest/smallest to current largest/smallest
        # if only bigger/smaller than second biggest/smallest just set that one
        smallOne, smallTwo = float("inf"), float("inf")
        bigOne, bigTwo = 0, 0
        for n in nums:
            if n > bigOne:
                bigTwo = bigOne
                bigOne = n
            elif n > bigTwo:
                bigTwo = n
            if n < smallOne:
                smallTwo = smallOne
                smallOne = n
            elif n < smallTwo:
                smallTwo = n
                
        return (bigOne*bigTwo)-(smallOne*smallTwo)

