class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in nums:
            count[i]+=1
        index=0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[index] = i
                index+=1

        return nums
