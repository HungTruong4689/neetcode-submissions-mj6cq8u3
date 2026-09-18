class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r =0,0

        g = sorted(g)
        s = sorted(s)
        while l <len(g) and r < len(s):
            if g[l]<=s[r]:
                l+=1
                r+=1
            else:
                break
        return l