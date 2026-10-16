class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        area = [0]
        def helper(grid, r, c, visit):
            count=0
            if min(r, c) < 0 or r==rows or c==cols or (r, c) in visit or grid[r][c]==0:
                return 0
            visit.add((r, c))
            count+=1
            count+=helper(grid, r+1, c, visit)
            count+=helper(grid, r-1, c, visit)
            count+=helper(grid, r, c+1, visit)
            count+=helper(grid, r, c-1, visit)
            return count

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visit and grid[i][j]==1:
                    temp = helper(grid, i, j, visit)
                    area.append(temp)
        return max(area)