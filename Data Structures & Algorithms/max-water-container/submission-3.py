class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            length = r - l 
            h = min(heights[l], heights[r])

            res = max(res, h * length)

            # which ever is the minimum, should be moved
            if heights[l] == h:
                l += 1
            elif heights[r] == h:
                r -= 1
            else: 
                l += 1
                r -= 1

        return res