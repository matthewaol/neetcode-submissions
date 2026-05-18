class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while (l < len(s)) and (r >= 0):
            if self.alphaNum(s[l]) and self.alphaNum(s[r]): # if both valid, compare value
                if (s[l].lower() == s[r].lower()):
                    r -= 1
                    l += 1
                else:
                    return False
            elif (self.alphaNum(s[l]) and not self.alphaNum(s[r])):
                r -= 1
            elif (not self.alphaNum(s[l]) and self.alphaNum(s[r])):
                l += 1
            else:                    
                r -= 1
                l += 1

        return True
                




    

    
    
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


