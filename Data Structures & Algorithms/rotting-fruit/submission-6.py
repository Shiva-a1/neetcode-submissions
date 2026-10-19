from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i, j))
        time = 0
        while queue and fresh>0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbor:
                    if 0<=r+dr<rows and 0<=c+dc<cols and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc]=2
                        fresh-=1
                        queue.append((r+dr, c+dc))
            time+=1
        return time if fresh==0 else -1