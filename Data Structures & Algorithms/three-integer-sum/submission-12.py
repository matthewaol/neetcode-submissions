class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # left pointer anchor approach
        res = []

        if len(nums) < 3:
            return res
        
        nums.sort() # sort first
        
        # iterate the left pointer
        # have j pointer directlry on the right of it and the k pointer at the leftmost element of the array
        i = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]  

                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return res
