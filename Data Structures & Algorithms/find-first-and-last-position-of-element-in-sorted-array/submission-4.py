class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        res = []
        m1,m2 = -1,-1
        while l<=r:
            if nums[l] == target:
                m1 = l
            else:
                l+=1
            if nums[r]== target:
                m2 = r
            else:
                r-=1
            print("l,r ",l,r)
            print("m1,m2 ",m1,m2)
            if nums[l] == target and nums[r]== target:
                m1= l
                m2 = r
                break
            else:
                continue
            
        return [m1,m2]