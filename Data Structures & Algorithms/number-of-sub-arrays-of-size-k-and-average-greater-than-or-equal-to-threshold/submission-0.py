from collections import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window = deque()
        total = 0
        l = 0
        for r in range(len(arr)):
            if r-l+1 > k:
                window.popleft()
                total-=arr[l]
                l+=1
            window.append(arr[r])
            total += arr[r]
            if len(window)==k:
                if total / k >= threshold:
                    count+=1
        return count
            