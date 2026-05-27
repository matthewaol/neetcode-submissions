class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        # pivot index: where the min element is.
        # then perform another binary search on the respective half

        # find the pivot
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]: # if the mid is greater than the highest num in right segment. 
            # so the pivot must be in the right half
                l = m + 1
            else:
                h = m
        p = l 

        def bsearch(start, end):
            while start <= end:
                m = (start + end) // 2

                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    start = m + 1
                else: 
                    end = m - 1

            return -1
            
        res = bsearch(0, p - 1)
        if res != -1:
            return res
        return bsearch(p, len(nums) - 1)


