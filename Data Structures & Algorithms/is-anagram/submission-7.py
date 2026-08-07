class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        s_se = Counter(s)
        t_se = Counter(t)

        return s_se == t_se

        
