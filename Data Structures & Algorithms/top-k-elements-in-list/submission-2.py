class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # list where the index represents the frequency, at that index we store the number
        # which appears exactly that i times.
        buckets = [[] for i in range(len(nums) + 1)]
        
        counts = Counter(nums)

        for n, count in counts.items():
            buckets[count].append(n)
        
        res = []
        for b in reversed(buckets):
            if b is not None:
                for n in b: 
                    res.append(n)
                    if len(res) == k:
                        return res
