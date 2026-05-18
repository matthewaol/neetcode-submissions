class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        bkts = [[] for i in range(len(nums) + 1)]

        for num, freq in c.items():
            bkts[freq].append(num)

        res = []

        for i in range(len(bkts) - 1, 0, -1):
            for n in bkts[i]:
                res.append(n)
                if len(res) == k:
                    return res