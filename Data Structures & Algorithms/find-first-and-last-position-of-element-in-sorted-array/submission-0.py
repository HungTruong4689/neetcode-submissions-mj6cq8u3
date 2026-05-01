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
        else:
            print(m)
            if len(nums)>=2 and nums[m-1] and nums[m-1] == target:
                return [m-1,m]
            elif len(nums)>=2 and nums[m+1] and nums[m+1] == target:
                return [m,m+1]
            else:
                return [m,m]