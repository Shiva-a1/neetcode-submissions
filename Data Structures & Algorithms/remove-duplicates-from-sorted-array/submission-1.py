class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        if len(nums)<=1:
            return len(nums)
        count=1
        for r in range(len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                nums[l]=nums[r]
                count+=1
        return count