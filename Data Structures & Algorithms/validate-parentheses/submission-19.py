class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        if s and (s[0] == '}' or s[0] == ')' or s[0] == ']'):
            return False

        st = []


        for i in range(len(s)):
            c = s[i]

            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if not st:
                    return False

                opening = st.pop()

                if opening == '(' and c != ')' or opening == '[' and c != ']' or opening == '{' and c != '}':
                    return False

        return len(st) == 0 
                

            