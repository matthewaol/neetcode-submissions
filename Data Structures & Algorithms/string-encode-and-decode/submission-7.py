class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        prefix = "#"
        # 5#Hello5#World

        for s in strs:
            length = len(s)
            res += str(length) + prefix + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr_s = ""
        i = 0

        while i < len(s): 
            if s[i].isdigit():
                # first, parse out the size
                size = ""
                while s[i] != "#":
                    size += s[i]
                    i += 1
                # 5#Hello5#World
                st = ""
                i += 1
                j = i
                while i < len(s) and i < j + int(size):
                    print(int(size), i)
                    st += s[i]
                    i += 1
                
                res.append(st)
            
        return res
