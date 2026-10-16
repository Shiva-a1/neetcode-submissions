class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def helper(grid, r, c, visit):
            if min(r, c)<0 or r==rows or c==cols or (r, c) in visit or grid[r][c]=='0':
                return
            else:
                visit.add((r, c))

            helper(grid, r+1, c, visit)
            helper(grid, r-1, c, visit)
            helper(grid, r, c+1, visit)
            helper(grid, r, c-1, visit)

            return


        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visit and grid[i][j]=='1':
                    count+=1
                    helper(grid, i, j, visit)
        return count