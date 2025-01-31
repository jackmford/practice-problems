class Solution:
    def isHappy(self, n: int) -> bool:

        m = set()

        total = 0
        while n != 1:
            # Get output num
            while n:
                d = n%10
                d = d**2
                n = n//10
                total+=d 

            # Can do it this way too
            # s = str(n)
            # print(s)
            # for c in s:
                # total += int(c)*int(c) 
            
            n = total
            if n in m:
                return False

            m.add(n)
            total = 0

        return True

        
