class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        total, count = 0, 0
        for i in nums:
            total += i
            count += dic[total - k]
            dic[total] += 1
        return count
