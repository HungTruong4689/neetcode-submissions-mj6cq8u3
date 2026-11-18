class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if i >0 and a == nums[i-1]:
                continue
            l=i
            r=len(nums)-1
            while l<r:
                cumSum = a + nums[l]+nums[r]
                if cumSum < 0:
                    l+=1
                elif cumSum >0:
                    r-=1
                if cumSum == 0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l <r:
                        l+=1

        return res

        