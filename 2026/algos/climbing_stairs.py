class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}

        def dfs(steps):
            if steps in self.memo:
                return self.memo[steps]
            if steps == n:
                return 1
            if steps > n:
                return 0

            one = dfs(steps + 1)
            two = dfs(steps + 2)
            self.memo[steps] = one + two
            return one + two

        return dfs(0)
