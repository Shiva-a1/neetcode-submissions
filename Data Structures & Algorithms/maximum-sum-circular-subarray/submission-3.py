class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best, worst = nums[0], nums[0]
        currSumMin = 0
        currSumMax = 0
        for i in range(len(nums)):
            currSumMax = max(0, currSumMax)
            currSumMin = min(0, currSumMin)
            currSumMax += nums[i]
            currSumMin += nums[i]
            best = max(currSumMax, best)
            worst = min(currSumMin, worst)
        return best if best < 0 else max(best, sum(nums) - worst)