class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        s = list(set(nums))
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)
        