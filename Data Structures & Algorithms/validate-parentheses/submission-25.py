class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        st = []

        hm = {")": "(", "}":"{", "]":"["}
        for c in s:
            if c == "[" or c == "(" or c == "{":
                st.append(c)
            else:
                if st and st[-1] == hm[c]:
                    st.pop()
                else:
                    return False

        return len(st) == 0
            
            
        