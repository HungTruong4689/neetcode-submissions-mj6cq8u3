class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        nums0 = []
        for i in nums:
            if i == 0:
                nums0.append(i)
            else:
                nums1.append(i)
        new_list = nums1+nums0
        nums = new_list[:]
        