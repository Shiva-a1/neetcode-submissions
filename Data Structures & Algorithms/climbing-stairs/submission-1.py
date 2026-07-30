class Solution:
    def climbStairs(self, n: int) -> int:
        # sum = 0
        # if n<=1:
        #     return 1
        # return sum + self.climbStairs(n-1) + self.climbStairs(n-2)
        memo = {}
        def helper(n):
            if n<=1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)