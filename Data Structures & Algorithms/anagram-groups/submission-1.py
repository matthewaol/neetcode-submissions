class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        
        for s in strs:
            sorted_s = "".join(sorted(s))
            hmap.setdefault(sorted_s, []).append(s)

        return list(hmap.values())