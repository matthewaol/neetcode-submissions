class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = 0
        while l < r:
            length = r - l
            h = min(heights[r], heights[l])
            area = h * length
            max_area = max(area, max_area)

            if h == heights[r]:
                r -= 1
                
            else:
                l += 1


        return max_area