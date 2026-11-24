class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 +7
        for i,val in enumerate(nums):
            r = len(nums)-1
            while i<=r and val + nums[r]>target:
                r-=1
            if i <=r:
                res += (2**(r-i))%mod
        return res