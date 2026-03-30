class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        def twoSum(arr,value):
            dic = {}
            target = 0 - value
            for i in arr:
                if i in dic:
                    res.append([value,dic[i],i])
                else:
                    dic[target - i] =i
        for i in range(len(nums)-2):
            twoSum(nums[i+1:],nums[i])
        reD = []
        seen= set()
        for lst in res:
            t = tuple(sorted(lst))
            if t not in seen:
                reD.append(t)
                seen.add(t)

        return reD

        