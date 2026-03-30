class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        f = 0
        res =1
        nums = sorted(nums)
        for i in range(1,len(nums)):
            f += (nums[i] - nums[i-1]) *i
            print(f)
            if f <=k:
                res +=1
        return res