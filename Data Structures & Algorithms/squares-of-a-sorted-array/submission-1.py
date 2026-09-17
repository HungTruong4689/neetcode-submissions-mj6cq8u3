class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0 , len(nums)-1
        result = []
        while l <=r:
            lsq = nums[l]**2
            rsq = nums[r]**2
            if lsq <=rsq:
                result.append(rsq)
                r-=1
            else:
                result.append(lsq)
                l+=1
        return result[::-1]

