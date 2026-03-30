class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res =1
        des = 1
        inc =1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                inc +=1
                des =1
            elif nums[i]>nums[i+1]:
                des +=1
                inc =1
            else:
                des =1
                inc =1
            res = max(res,des,inc)
        return res
        
                
