class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = cumSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<= nums[i-1]:
                cumSum =0
            cumSum += nums[i]
            res = max(cumSum,res)
        return res
