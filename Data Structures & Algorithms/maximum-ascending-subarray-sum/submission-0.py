class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res =0
        inc =0
        des =0
        for i in range(len(nums)-1):
            
            if nums[i]<nums[i+1]:
                inc += nums[i]
                des =0
            else:
                if des >0:
                    inc =0
                else:
                    inc += nums[i]
                    res = max(res,inc)
                    inc = 0
                des += nums[i]    
            if i + 1 == len(nums)-1 and inc >0:
                inc += nums[i+1]
            res = max(res,inc)
        return res
