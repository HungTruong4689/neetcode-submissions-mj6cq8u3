class Solution:
    def maxScore(self, s: str) -> int:
        sC = 0
        l,r = 0,0
        for i in s:
            r += int(i)
        for j in range(len(s)-1):
            if s[j]=='0':
                l+=1
            else:
                r -=1
            sC = max(sC,l+r)
        return sC
            