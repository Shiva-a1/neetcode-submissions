import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # Solution 1
        # import math
        # def distance(x, y):
        #     return math.sqrt((x-0)**2 + (y-0)**2)
        # def helper(arr, s, e):
        #     if not arr:
        #         return []
        #     if e-s+1<=1:
        #         return arr
        #     pivot = distance(arr[e][0], arr[e][1])
        #     left = s
        #     for i in range(s, e):
        #         if distance(arr[i][0], arr[i][1])<pivot:
        #             arr[i], arr[left] = arr[left], arr[i]
        #             left+=1
        #     arr[left], arr[e] = arr[e], arr[left]
        #     helper(arr, s, left-1)
        #     helper(arr, left+1, e)
        #     return arr
        # helper(points, 0, len(points)-1)
        # return points[:k]

        # Solution 2 using Heap
        
        def distance(x, y):
            return math.sqrt((x-0)**2 + (y-0)**2)
        # dic = {}
        # for i in range(len(points)):
        #     dist = distance(points[i])
        #     if dist in dic:
        #         dic[dist].append(points[i])
        #     else:
        #         dic[dist] = [points[i]]
        # self.heap = list(dic)

        # res = []
        # while len(res) < k:
        #     for pt in dic[ind]:
        #         res.append(pt)
        #         if len(res) == k:
        #             break
        # return res
        minHeap = []
        for x, y in points:
            dist = distance(x, y)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res