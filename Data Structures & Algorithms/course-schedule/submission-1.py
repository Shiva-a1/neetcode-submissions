class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        path, safe = set(), set()

        def dfs(course):
            if course in path:
                return False
            if course in safe:
                return True
            path.add(course)
            for nxt in adj[course]:
                if not dfs(nxt):
                    return False
            path.remove(course)
            safe.add(course)
            return True

        return all(dfs(c) for c in range(numCourses))
