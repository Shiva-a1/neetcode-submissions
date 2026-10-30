class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        count = {}
        for r in range(0, len(nums)):
            if nums[r] in count:
                if count[nums[r]]<2 and l==r:
                    count[nums[r]]+=1
                    l+=1
                if count[nums[r]]<2 and l!=r:
                    count[nums[r]]+=1
                    nums[l] = nums[r]
                    l+=1
                
            else:
                count[nums[r]] = 1
                nums[l]=nums[r]
                l+=1
        return l