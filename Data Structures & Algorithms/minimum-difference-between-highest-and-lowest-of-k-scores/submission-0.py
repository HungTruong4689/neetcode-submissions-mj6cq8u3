class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mV = float('inf')
        hi, lo = 0,0
        for i in range(k-1,len(nums)):
            lo = nums[i-k+1]
            hi = nums[i]
            
            mV= min(mV,hi-lo)
            print(i,i-k,hi-lo,mV)
        return mV