class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            comp = target - nums[i] # computing the compliment
            print("nums[i]:", nums[i])
            print("comp: ", comp)

            if comp not in hm: # store the compliment hm
                hm[nums[i]] = i  
            else:
                return [hm[comp], i]
        
        return []
            