class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        l,r=0, len(nums)-1
        while l<=r:
            k = (l+r)//2
            if nums[k]==target:
                return True
            if nums[k]>target:
                r=k-1
            if nums[k]<target:
                l=k+1
        return False