class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            encoded = str(len(s)) + '#' + s
            res.append(encoded)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            leng = int(s[i:j])
            i = j + 1
            j = i + leng
            res.append(s[i:j])
            i = j
            
        return res



