class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        big_list=[]
        l = []
        def helper(start, nums, remaining):
            if remaining == 0:
                    big_list.append(l[:])
            if remaining < 0:
                    return
            
            for i in range(start, len(nums)):
                l.append(nums[i])
                helper(i, nums, remaining - nums[i])
                l.pop()
            return
        helper(0, nums, target)
        return big_list
            