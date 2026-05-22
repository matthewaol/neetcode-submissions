class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()

        maxLen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            
            se.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen