class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0]*cols
        for r in range(rows-1, -1, -1):
            currRow = [0]*cols
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                elif r == rows - 1 and c == cols - 1:
                    currRow[c] = 1
                else:
                    right = currRow[c+1] if c + 1 < cols else 0
                    down = prevRow[c]
                    currRow[c] = right + down
            prevRow = currRow
        return prevRow[0]