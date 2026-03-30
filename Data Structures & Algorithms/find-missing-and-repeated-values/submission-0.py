class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0]* (n*n +1)
        res = []
        for i in range(n):
            for j in grid[i]:
                arr[j] +=1
        a = 0
        b=0
        for m in range(1,len(arr)):
            if arr[m] ==2:
                a = m
            if arr[m] ==0:
                b = m
        res.extend([a,b])
        return res