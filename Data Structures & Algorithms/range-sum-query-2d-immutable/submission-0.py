class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        total = 0
        self.prefix = []
        for r in range(len(matrix)):
            total = 0
            row = []
            for c in range(len(matrix[0])):
                if r==0:
                    total += matrix[r][c]
                elif c==0:
                    total += self.prefix[r-1][c] + matrix[r][c]
                else:
                    total = self.prefix[r-1][c] + row[c-1] + matrix[r][c] - self.prefix[r-1][c-1]
                row.append(total)
            self.prefix.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre_second = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        corner = self.prefix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        return (pre_second - above - left + corner)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)