class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        res = 0
        s = set(nums)

        i = 0
        while i < len(nums):
            n = nums[i]
            if n - 1 not in s: # if num - 1 is not in the array, we have the start of a sequence
                j = 0
                while n + j in s:
                    seq += 1
                    j += 1
                    
            res = max(seq, res)
            seq = 0
            i += 1
        return res


        
        