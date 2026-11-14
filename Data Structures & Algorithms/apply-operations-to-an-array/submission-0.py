class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
                nums[r-1] *=2
                nums[r] = 0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums
