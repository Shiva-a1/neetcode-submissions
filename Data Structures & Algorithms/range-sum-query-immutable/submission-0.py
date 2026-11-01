class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefix = []
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preLeft = self.prefix[left-1] if left>0 else 0
        preRight = self.prefix[right]
        return (preRight - preLeft)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)