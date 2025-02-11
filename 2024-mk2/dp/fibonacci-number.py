class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.memo:
            return self.memo[n]

        res = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = res
        
        return res
        
