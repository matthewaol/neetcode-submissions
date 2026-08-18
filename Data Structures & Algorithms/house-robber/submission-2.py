class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp - bottom-up
        # create an array to represent the answer step-by-step
        # by each index, we store the highest amount of money 
        # we can obtain up until each index
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


        