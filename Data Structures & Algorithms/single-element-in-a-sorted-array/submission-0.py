class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,1
        while r< len(nums):
            if nums[l] == nums[r]:
                l+=2
                r+=2
            else:
                return nums[l]
        return 0