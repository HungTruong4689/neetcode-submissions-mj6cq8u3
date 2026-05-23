class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        dt = [abs(val - x) for val in arr]
        
        # Start at the closest element
        mid_val = min(dt)
        idx = dt.index(mid_val)
        
        res = [arr[idx]]
        l, r = idx - 1, idx + 1
        
        # Continue until we have k elements
        while len(res) < k:
            # If left is valid AND (right is invalid OR left is closer/equal)
            if l >= 0 and (r >= n or dt[l] <= dt[r]):
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
        
        res.sort()
        return res