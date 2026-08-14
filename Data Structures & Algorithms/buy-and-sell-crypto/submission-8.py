class Solution:
    # buy low, sell high
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for l in range(len(prices) - 1):
            r = l + 1
            while r < len(prices) and prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
                r += 1
                

        return res

