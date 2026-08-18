class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            curr, prev = 0, 0

            for n in nums:
                curr, prev = max(curr, prev + n), curr
            
            return curr
        
        return max(helper(nums[1:len(nums)]), helper(nums[0:len(nums) - 1]))