class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        smallest_word = min(strs) # use this word for indices


        found_evil = False
        for i in range(len(smallest_word)): 
            char = smallest_word[i]

            for s in strs:
                if not (i < len(s)) or s[i] != char:
                    found_evil = True
            
            if not found_evil:
                res += char
        
        return res

            
