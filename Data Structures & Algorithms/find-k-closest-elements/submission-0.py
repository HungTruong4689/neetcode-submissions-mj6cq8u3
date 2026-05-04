class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        dt = [0]*n
        res = []
        for i in range(len(arr)):
            dt[i] = abs(arr[i]-x)
        mid = min(dt)
        index = dt.index(mid)
        res.append(arr[index])
        l,r = index -1 , index +1
        while l>=0 or r<= len(arr)-1:
            le = len(res)
            if le <k:
                if dt[l] <= dt[r]:
                    res.append(arr[l])
                    l-=1
                else:
                    res.append(arr[r])
                    r+=1
            else:
                break 
        res.sort()
        return res
