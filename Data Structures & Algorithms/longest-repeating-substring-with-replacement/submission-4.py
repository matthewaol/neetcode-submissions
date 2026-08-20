class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freqs = {}
        res = 0

        max_freq = 0
        l = 0
        for r in range(len(s)):
            char_freqs[s[r]] = char_freqs.get(s[r], 0) + 1
            max_freq = max(max_freq, char_freqs[s[r]]) # keeping track of the highest frequency character

            while (r - l + 1) - max_freq > k:
                char_freqs[s[l]] -= 1 
                l += 1
            
            res = max(r - l + 1, res)
        
        return res
            

        
            

            




        