class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        preSum = [0]* len(nums)
        postSum = [0]* len(nums)
        total_left = 0
        total_right = 0
        for i in range(l):
            total_left+= nums[i]
            preSum[i] = total_left
            total_right+= nums[l-1-i]
            postSum[l-i-1] = total_right
        for pivot in range(l):
            left_sum = preSum[pivot-1] if pivot > 0 else 0
            right_sum = postSum[pivot+1] if pivot < l-1 else 0
            if left_sum == right_sum:
                return pivot
        return -1