class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0

        hm_t = {} # gather the counts for hm_t
        for c in t:
            hm_t[c] = hm_t.get(c, 0) + 1

        hm_s = {} # keep track of the char frequencies of s
        l = 0

        have = 0
        need = len(hm_t)

        res = [-1, -1]
        resLen = float('infinity')
        for r in range(len(s)):
            if s[r] in hm_t:
                hm_s[s[r]] = hm_s.get(s[r], 0) + 1 # expand the window

                if hm_s[s[r]] == hm_t[s[r]]:
                    have += 1

            while have == need:
                # check if the current res is smaller, then update
                if r - l + 1 < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1
                
                if s[l] in hm_s:
                    hm_s[s[l]] -= 1
                    if hm_s[s[l]] < hm_t[s[l]]:
                        have -= 1
                        
                l += 1

        return s[res[0]:res[1]] if resLen != float('infinity') else ""
