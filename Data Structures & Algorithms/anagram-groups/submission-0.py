class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            # use string as a key, 
            
            key = str(sorted(s))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(s)
        
        return list(hmap.values())