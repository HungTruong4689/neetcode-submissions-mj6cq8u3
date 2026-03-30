class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        l,r = 0,0
        if len(s) ==1:
            return 1
        while r<len(s):
            m = s[l:r]
            print(m)
            while s[r] in s[l:r]:
                l+=1
                
            r+=1
            print(m,len(m))
            if len(m)>=len(res):
                res = m

        return len(res)
            