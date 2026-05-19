class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cash = 0
        if len(prices) < 2:
            return 0 

        l = 0
        r = l + 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_cash = max(profit, max_cash)
            else:
                l = r
            r += 1
        return max_cash
        
