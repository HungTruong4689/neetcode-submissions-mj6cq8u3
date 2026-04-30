class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l = []
        for i in range(1,len(nums)):
            val = nums[i] - nums[i-1]
            if val not in l:
                l.append(val)
        l.sort()
        print(l)
        return max(l[:p])