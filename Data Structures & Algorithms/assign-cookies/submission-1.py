class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r =0,0
        k = 0
        for j in s:
            for i in g:
                if j>=i:
                    k+=1
                    g.remove(i)

        return k