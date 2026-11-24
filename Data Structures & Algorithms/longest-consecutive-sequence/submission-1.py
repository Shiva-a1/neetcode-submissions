class UnionFind:
    def __init__(self, nums):
        self.par = {}
        self.rank = {}

        for i in nums:
            self.par[i] = i
            self.rank[i] = 1

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1==p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.par[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Approach 1: Solving using Hash Set
        # s = set(nums)
        # best = 0
        # for n in s:
        #     if n-1 not in s:
        #         length = 1
        #         while n+length in s:
        #             length +=1
        #         best = max(best, length)
        # return best

        # Approach 2: Solving using Union-Find
        s = set(nums)
        uf = UnionFind(s)
        for n in s:
            if n+1 in s:
                uf.union(n, n+1)
        return max((uf.rank[uf.find(n)] for n in s), default = 0)
