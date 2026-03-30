class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s = {}
        for i in arr:
            if i not in s:
                s[i] = 0
            s[i] +=1
        nums = []
        for key,value in s.items():
            if value ==1:
                nums.append(key)
        print(nums)
        if k<= len(nums):
            return nums[k-1]
        else:
            return ""