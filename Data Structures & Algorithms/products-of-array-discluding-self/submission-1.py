class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = [1]*len(nums)
        for r in range(1, l):
            arr[r] = arr[r-1] * nums[r-1]
        prod = 1
        for r in range(l-2, -1, -1):
            prod *= nums[r+1]
            arr[r] *= prod
        return arr