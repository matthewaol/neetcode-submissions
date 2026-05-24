class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        res = float('infinity')

        while l <= h:
            m = (l + h) // 2
            res = min(res, nums[m])


            if nums[l] > nums[h] and nums[m] > nums[h]:
                l = m + 1 # ignore the left part
            else: 
                h = m - 1 # ignore the right part

        return res 
        