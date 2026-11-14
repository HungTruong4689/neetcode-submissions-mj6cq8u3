class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        
            
        for r in range(len(nums)):
            if r <len(nums)-1 and nums[r] == nums[r+1]:
                nums[r] *=2
                nums[r+1] = 0
            if nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums
