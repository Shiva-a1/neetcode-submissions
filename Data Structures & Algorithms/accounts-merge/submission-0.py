class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        owner = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in owner:
                    uf.union(i, owner[email])
                else:
                    owner[email] = i
        groups = defaultdict(list)
        for email, i in owner.items():
            groups[uf.find(i)].append(email)
        return [[accounts[i][0]] + sorted(emails) for i, emails in groups.items()]