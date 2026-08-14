class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if we hit a duplicate character then shrink the string and - from the length
        se = set()
        length = 0

        # default is to expand the window by incrementing r and adding that character.
        # if we add an r and that's already in the window, then we start incrementing l and reducing
        # the size, until the duplicate is gone.
        l = 0
        for r in range(len(s)):
            if s[r] not in se:
                se.add(s[r])
            else: 
                while s[r] in se:
                    se.remove(s[l])
                    l += 1
                se.add(s[r])
            length = max(length, r - l + 1)

        return length

