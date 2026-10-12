import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # # Solution 1
        # self.heap = stones[:]
        # heapq.heapify(self.heap)
        # while len(self.heap) > 1:
        #     temp = []
        #     while len(self.heap) > 2:
        #         temp.append(self.heap[0])
        #         heapq.heappop(self.heap)

        #     if self.heap[0] == self.heap [1]:
        #         self.heap = temp
        #     elif self.heap[0]< self.heap[1]:
        #         temp.append(self.heap[1] - self.heap[0])
        #     else:
        #         temp.append(self.heap[0] - self.heap[1])
        #     self.heap = temp
        #     heapq.heapify(self.heap)
        # return self.heap.pop() if self.heap else 0

        # Solution 2
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y!=x:
                heapq.heappush(stones, -(y-x))

        return -stones[0] if stones else 0





