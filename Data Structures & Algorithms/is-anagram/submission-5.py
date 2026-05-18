class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        print(count_t)
        print(count_s)
        return count_t == count_s 