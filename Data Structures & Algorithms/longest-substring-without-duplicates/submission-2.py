class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        l,r = 0,1
        if len(s) ==1:
            return 1
        while r<len(s):
            m = s[l:r]
            if s[l] == s[r]:
                l+=1
            while s[r] in s[l:r]:
                l+=1
                
            r+=1
            print(m)
            if len(m)>=len(res):
                res = m

        return len(res)
            