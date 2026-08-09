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

        for i in range(len(bkts) - 1, 0, -1):
            while bkts[i]:
                res.append(bkts[i].pop())
                if len(res) == k:
                    return res

        return res
        

        




        


        





        


