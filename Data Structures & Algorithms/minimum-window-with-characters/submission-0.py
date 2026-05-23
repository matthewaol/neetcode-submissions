class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float("infinity")
        substr = ""
        l = 0

        t_freq = Counter(t)
        substr_freq = {}
        have = 0
        need = len(t_freq)

        for r in range(len(s)):
            # Everytime we have a character(s) we should increment the have counter
            substr_freq[s[r]] = substr_freq.get(s[r], 0) + 1

            if (s[r] in t_freq and substr_freq[s[r]] == t_freq[s[r]]):
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                substr_freq[s[l]] -= 1

                if s[l] in t_freq and substr_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1


        return s[res[0]:res[1] + 1]