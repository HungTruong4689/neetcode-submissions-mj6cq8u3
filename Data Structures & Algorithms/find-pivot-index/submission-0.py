class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lS = 0
        rS = sum(nums[1:])
        if lS == rS:
            return 0
        for i in range(1,len(nums)):
            lS += nums[i-1]
            rS -= nums[i]
            print(lS,rS)
            if lS == rS:
                return i
        
        return -1