class Solution:
    def countSubstrings(self, s: str) -> int:
        # substring s[i..j]
        n = len(s)
        res = 0
        
        dp = [[False] * n for _ in range(n)]


        for i in range(n - 1, -1, -1): # coming from top, decrementing
            for j in range(i, n): # starting same position as i, incrementing
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j-1] == True):
                    dp[i][j] = True
                    res += 1
        
        return res