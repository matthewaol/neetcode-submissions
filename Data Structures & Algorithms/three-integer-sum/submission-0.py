class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) < 3):
            return []

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a: # a duplicate start of a sequence
                continue

            l = i + 1 
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + a == 0:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] + a < 0:
                    l += 1
                elif nums[l] + nums[r] + a > 0:
                    r -= 1

        return res


            

