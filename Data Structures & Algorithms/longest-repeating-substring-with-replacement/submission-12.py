class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hm = {}
        res = 0
        most_freq_char_cnt = 0
        
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1 

            len_window = r - l + 1
            most_freq_char_cnt = max(hm[s[r]], most_freq_char_cnt)
            num_replacements = len_window - most_freq_char_cnt

            while l < r and (r - l + 1) - most_freq_char_cnt > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res








