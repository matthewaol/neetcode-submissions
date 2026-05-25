class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm and abs(i - hm[nums[i]]) <= k:
                return True 
            
            hm[nums[i]] = i
            
        return False
       
        