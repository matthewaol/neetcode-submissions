class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            arr = [0] * 26

            for c in s:
                i = ord(c) - 97 # -97 because ord returns ordinal, which starts at 96. so ord('a') = 96 
                arr[i] += 1

            key = tuple(arr)

            if key not in hm:
                hm[key] = []
            hm[key].append(s)
        
        return list(hm.values())
            



                


        
    