class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def helper(l, r, heights):
            area = min(heights[l], heights[r]) * (r-l)
            return area
        
        l = 0
        r = len(heights) - 1
        max_area = helper(l, r, heights)
        while l<r:
            max_area = max(max_area, helper(l, r, heights))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area
        
