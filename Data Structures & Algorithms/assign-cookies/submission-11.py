class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r =0,0
        k = 0
        g = sorted(g)
        s = sorted(s)
        while l < len(g) and r < len(s):
            if s[r]>= g[l]:
                l+=1
            
            r+=1    

        return l