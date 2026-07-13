class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_array = []
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                count_array.append(count)
                count = 0
        count_array.append(count)
        max_element = 0
        for i in count_array:
            if i>max_element:
                max_element = i
        return max_element