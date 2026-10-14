import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = [-x for x in nums]
        heapq.heapify(self.heap)
        self.k = k
        while self.k>1:
            heapq.heappop(self.heap)
            self.k-=1
        return -heapq.heappop(self.heap)