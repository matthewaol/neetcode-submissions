class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []


        for n in nums:
            heapq.heappush(hp, n * -1)

        for _ in range(k):
            res = heapq.heappop(hp)

        return res * -1