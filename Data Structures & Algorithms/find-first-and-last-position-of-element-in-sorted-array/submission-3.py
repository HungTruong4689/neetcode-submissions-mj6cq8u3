class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        res = []
        m = -1
        while l<=r:
            k = (l+r)//2
            if nums[k] == target:
                m = k
                break
            if nums[k]>target:
                r = k -1
            if nums[k]<target:
                l = k+1
        if m == -1:
            return [-1,-1]
        l1,r1 = 0,m
        l2,r2 = m,len(nums)-1
        m1,m2=-1,-1
        while l1<=r1:
            k1 = (l1+r1)//2
            if nums[k1] == target:
                m1 = k1
                
            if nums[k1]>=target:
                r1 = k1 -1
            if nums[k1]<=target:
                l1 = k1+1
        while l2<=r2:
            k2 = (l2+r2)//2
            if nums[k2] == target:
                m2 = k2
                
            if nums[k2]>=target:
                r2 = k2 -1
            if nums[k2]<=target:
                l2 = k2+1
        return [m1,m2]