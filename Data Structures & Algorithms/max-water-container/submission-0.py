class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l1,r1 = 0, len(heights)-1
        l2,r2 = 0, len(heights)-1
        while r1 >0 and l2< len(heights):
            a1 = (r1-l1)* min(heights[r1],heights[l1])
            print(a1)
            area = max(area,a1)
            r1 -=1
            a2 = (r2-l2)* min(heights[r2],heights[l2])
            area = max(area,a2)
            l2 +=1
        return area