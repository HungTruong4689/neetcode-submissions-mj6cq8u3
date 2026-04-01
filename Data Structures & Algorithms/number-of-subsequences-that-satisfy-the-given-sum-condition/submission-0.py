class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l,r = 0 ,0
        res = 0
        while l < len(nums):
            for j in range(l,len(nums)):
                mi = min(nums[l],nums[j])
                ma = max(nums[l],nums[j])
                print(mi,ma)
                if mi + ma <= target:
                    res+=1
                    if j - l>=2:
                        res +=1
            l+=1
        return res