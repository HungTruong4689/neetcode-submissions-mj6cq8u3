class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1,r1 = 0, len(nums)-1
        l2,r2 = 0, len(nums)-1
        res = [0]*len(nums)
        while l1<len(nums):
            if nums[l1]<pivot:
                res[l2] =nums[l1]
                l2+=1
            if nums[r1]>pivot:
                res[r2]=nums[r1]
                r2-=1
            l1+=1
            r1-=1
        while l2<=r2:
            res[l2]=res[r2]=pivot
            l2+=1
            r2-=1
        return res
