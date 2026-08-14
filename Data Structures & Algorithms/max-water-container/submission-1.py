class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            min_beam = min(heights[l], heights[r])
            res = max(res, min_beam * (r - l))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1            
            else:
                l += 1
                r -= 1
        return res

            
        