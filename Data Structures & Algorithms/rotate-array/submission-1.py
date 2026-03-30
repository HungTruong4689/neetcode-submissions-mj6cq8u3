class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        print(n)
        nums[:] = nums[len(nums)-n:] + nums[:len(nums)-n] 
        