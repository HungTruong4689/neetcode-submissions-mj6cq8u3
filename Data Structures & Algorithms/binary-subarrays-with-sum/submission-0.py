class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        l,r = 0,1
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i,len(nums)):
                cur += nums[j]
                if cur == goal:
                    res +=1
        return res
