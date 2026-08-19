class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fewer coins -> making
        cache = {}

        def dfs(amount):
            if amount in cache:
                return cache[amount]

            if amount == 0:
                return 0 

            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            
            cache[amount] = res

            return cache[amount]
            
        minCoin = dfs(amount)

        if minCoin >= 1e9:
            return -1
        return minCoin

        
        