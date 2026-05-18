class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i, j = 0,1
        while i < len(nums):
            while j < len(nums):
                print(nums[i], nums[j])
                if nums[i] == nums[j]:
                    return True
                j+=1
            j=i+2
            i+=1
        
        return False

            