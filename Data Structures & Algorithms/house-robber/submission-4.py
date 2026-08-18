class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0, 0 

        # [rob1, rob2, n, n + 1, n + 2...]
        for n in nums:
            # temp = max(rob1 + n, rob2) # max of rob1 + n and rob2
            # rob1 = rob2 # progress the pointers: rob1 to rob2
            # rob2 = temp # and rob2 to temp
            curr, prev = max(prev + n, curr), curr
        
        return curr
        
            