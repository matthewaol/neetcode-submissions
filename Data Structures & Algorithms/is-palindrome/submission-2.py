class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:
            if self.alphaNum(s[i]) and self.alphaNum(s[j]): 
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not self.alphaNum(s[i]):
                i += 1
            elif not self.alphaNum(s[j]):
                j -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))