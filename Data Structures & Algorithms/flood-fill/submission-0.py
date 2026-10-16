class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()
        ini_val = image[sr][sc]
        def helper(image, r, c, visit, color):
            if min(r, c)<0 or r==rows or c==cols or (r, c) in visit or image[r][c] != ini_val:
                return
            visit.add((r, c))
            image[r][c] = color
            helper(image, r+1, c, visit, color)
            helper(image, r-1, c, visit, color)
            helper(image, r, c+1, visit, color)
            helper(image, r, c-1, visit, color)

        helper(image, sr, sc, visit, color)
        return image
            