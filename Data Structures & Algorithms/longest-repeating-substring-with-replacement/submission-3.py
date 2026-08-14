class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hm = {}
        res = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1 # expand the window

            len_window = r - l + 1
            most_freq_char_cnt = max(hm.values())
            num_replacements = len_window - most_freq_char_cnt

            if num_replacements > k:
                # shrink the window
                while l < r and num_replacements > k:
                    hm[s[l]] -= 1
                    l += 1
                    num_replacements = (r - l + 1) - max(hm.values())
            
            res = max(res, r - l + 1)

        return res






