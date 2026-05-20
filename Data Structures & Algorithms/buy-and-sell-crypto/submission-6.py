class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) < 0:
            return 0

        l = 0
        r = 1

        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r

            r += 1

        return max_profit
            





        



       
