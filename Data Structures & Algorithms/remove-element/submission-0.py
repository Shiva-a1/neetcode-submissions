class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        count = 0
        temp_array=[]
        for i in range(len(nums)):
            if val != nums[i]:
                k +=1
                temp_array.append(nums[i])
            else:
                count+=1
        for i in range(count):
            temp_array.append('_')
        nums[:] = temp_array
        return k
