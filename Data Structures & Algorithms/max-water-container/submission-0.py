class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights)-1
        while(l<r):
            area = (r-l)*min(heights[r],heights[l])
            if area > maxarea:
                maxarea = area
            if heights[l]<=heights[r]:
                l = l+1
            elif heights[r]<heights[l]:
                r = r-1
        return maxarea

        