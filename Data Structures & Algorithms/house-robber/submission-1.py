class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def top_down(n, memo):
            if n<0:
                return 0
            if n in memo:
                return memo[n]
            take = nums[n] + top_down(n-2, memo)
            leave = top_down(n-1, memo)
            memo[n] = max(take, leave)
            return memo[n]
        return top_down(len(nums)-1, memo)