class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        res = [0] * n
        
        prefix[0] = 1
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] * nums[i - 1]

        suffix[n] = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
            
        for i in range(n):
            res[i] = suffix[i + 1] * prefix[i]
        return res 
