class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums * 2
        return ans
        # l = len(nums)
        # new_l = 2*l
        # ans = [0]*new_l
        # for i in range(l):
        #     ans[i] = nums[i]
        #     ans[i+l] = nums[i]
        # return ans