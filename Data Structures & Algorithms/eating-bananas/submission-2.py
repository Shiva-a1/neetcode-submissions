class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        piles.sort()
        def check(n):
            hr_count=0
            for p in piles:
                hr_count += math.ceil(p/n)
            return hr_count
        max_num = max(piles)
        
        def helper(low, high):
            min_val = high
            while low<=high:
                mid = (low+high)//2
                if mid == 0: low = 1; continue
                hrs = check(mid)

                if mid<min_val and hrs<=h:
                    min_val = mid
                    high = mid-1
                elif hrs>h:
                    low = mid+1
                else:
                    high = mid-1
            return min_val
        return helper(1, max_num)