class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hm = {}
        n = len(nums)

        for n in nums:
            if n not in hm:
                hm[n] = 1
            hm[n] += 1
        return max(hm, key=hm.get)

        
