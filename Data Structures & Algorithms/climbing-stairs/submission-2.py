class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def top_down(n, memo):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = top_down(n-1, memo) + top_down(n-2, memo)
            return memo[n]
        return top_down(n, memo)