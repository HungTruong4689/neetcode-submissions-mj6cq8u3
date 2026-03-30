class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        countDel = 0
        for i in range(len(s)):
            newStr = s[:i] + s[i+1:]
            print(newStr)
            if newStr == newStr[::-1]:
                return True
            
            
        return False
        