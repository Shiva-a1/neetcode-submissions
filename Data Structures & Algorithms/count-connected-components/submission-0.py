class UnionFind:
    def __init__(self, n) -> None:
        self.rank = {}
        self.par = {}
        self.num_components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, x) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def union(self, x, y) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.num_components -= 1
        return True
    
    def components(self):
        return self.num_components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.components()