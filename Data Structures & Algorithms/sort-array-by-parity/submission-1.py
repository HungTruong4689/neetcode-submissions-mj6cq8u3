class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, 0
        for k in range(len(nums)):
            if nums[k] %2 ==0:
                nums[l],nums[k]= nums[k],nums[l]
                l+=1
        return nums