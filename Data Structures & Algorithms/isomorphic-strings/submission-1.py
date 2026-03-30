class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        l = 0
        while l < len(s):
            if s[l] in dic:
                if dic[s[l]] != t[l]:
                    return False
            else:
                dic[s[l]] = t[l]
            l+=1
        r = 0
        dic2= {}
        while r < len(t):
            if t[r] in dic2:
                if dic[t[r]] != s[r]:
                    return False
            else:
                dic2[t[r]] = s[r]
            r+=1
        return True