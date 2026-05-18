class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_seq = 0
        seq = 0

        for n in nums:
            # if n doesn't have a n-1, its the start of a sequence
            if (n - 1) not in s:
                seq = 0
                while (seq + n) in s:
                    seq += 1
                    
                max_seq = max(max_seq, seq)


        return max_seq
                
                


                