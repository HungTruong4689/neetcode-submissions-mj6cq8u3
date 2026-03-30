class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(0,n-1):
            diff = ord(s[i+1]) - ord(s[i])
            result += abs(diff)
        return result