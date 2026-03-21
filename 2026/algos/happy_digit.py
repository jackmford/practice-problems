class Solution:
    def isHappy(self, n: int) -> bool:
        save = {}
        while n != 1:
            tmp = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                tmp = tmp + (digit**2)
            if tmp in save:
                return False
            n = tmp
            save[tmp] = True
        return True
