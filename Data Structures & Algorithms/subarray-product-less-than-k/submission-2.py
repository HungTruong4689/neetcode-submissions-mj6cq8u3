class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prePro =1
        l = 0
        res = 0
        for r in range(len(nums)):
            prePro *= nums[r]

            while prePro>=k:
                prePro //= nums[l]
                l+=1
            res += (r-l) +1
        return res
