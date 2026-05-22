class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        c_freq = {}
        max_freq = 0
        l = 0
        for r in range(len(s)):
            # Shrink the window, to remove 
            c_freq[s[r]] = c_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, c_freq[s[r]])

            while (r - l + 1) - max_freq > k: # if its valid (len of window - highest freq character -> gives the # of characters that are in the way)
                c_freq[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
