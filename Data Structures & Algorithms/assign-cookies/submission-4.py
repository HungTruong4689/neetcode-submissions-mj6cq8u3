class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r =0,0
        k = 0
        for j in range(len(s)):
            for i in range(len(g)):
                greed = g[i]
                cake = s[j]
                if greed>0 and cake>0 and cake>=greed:
                    k+=1
                    g[i] = 0
                    
                    

        return k