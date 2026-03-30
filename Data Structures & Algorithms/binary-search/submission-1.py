class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = int(len(nums) /2)
        print(m)
        if target == nums[m]:
            return m
        if len(nums)<=0 or (m==0 and nums[m] != target):
            return -1
        if target >nums[m]:
            return self.search(nums[m:],target)
        if target < nums[m]:
            return self.search(nums[:m],target)
        