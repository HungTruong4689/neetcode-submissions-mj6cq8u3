class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        l,r = 0,1
        if len(s) ==1:
            return 1
        while r<len(s):
            m = s[l:r]
            print(m,s[r])
            
            if s[r] in m:
                l+=1
                continue
            else:
                m += s[r]
            if len(m)>=len(res):
                res = m
            r+=1
            #print(m,len(m))
            

        return len(res)
            