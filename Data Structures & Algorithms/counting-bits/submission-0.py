class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(num):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            return count
        l = [0] * (n+1)
        for i in range(n+1):
            l[i] = helper(i)
        return l