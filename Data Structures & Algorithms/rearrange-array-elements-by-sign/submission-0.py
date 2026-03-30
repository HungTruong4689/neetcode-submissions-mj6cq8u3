class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        l, r,k = 0,0,0
        while l < len(nums):
            if l % 2 ==0:
                nums[l]=pos[r]
                r+=1
            else:
                nums[l]=neg[k]
                k+=1
            l+=1
        return nums
