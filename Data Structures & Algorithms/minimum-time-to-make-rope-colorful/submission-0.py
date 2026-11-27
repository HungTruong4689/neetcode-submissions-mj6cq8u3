class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1,len(colors)):
            if colors[r]==colors[l]:
                if neededTime[l]<= neededTime[r]:
                    res+= neededTime[l]
                    l+=1
                else:
                    res+= neededTime[r]
            else:
                l = r
        return res

