class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left, right = 0, len(s) - 1
        # while left < right:
        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        # ###############################
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
        # ###############################

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <=ord('Z') or
                ord('a') <= ord(c) <=ord('z') or
                ord('0') <= ord(c) <=ord('9'))
                
    
                    