class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bkts = [[] for i in range(len(nums) + 1)] 
        hm = {}
        # index represents the frequency

        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        for n, f in hm.items(): # so we can index k
            bkts[f].append(n)
        
        res = []
        for b in bkts: 
            if b:
                res.extend(b)
        
        
        return res[-k:]
        
        
        




        


        





        


