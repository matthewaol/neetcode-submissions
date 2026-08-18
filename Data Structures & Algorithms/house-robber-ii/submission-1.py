class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache2 = {}
        cache1 = {}
        nums1 = nums[0:len(nums) - 1]
        nums2 = nums[1:len(nums)]

        def dfs(ns, i, cache):
            if i >= len(ns):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(ns[i] + dfs(ns, i + 2, cache), dfs(ns, i + 1, cache))
            
            return cache[i]
        
        return max(dfs(nums1, 0, cache1), dfs(nums2, 0, cache2))
        