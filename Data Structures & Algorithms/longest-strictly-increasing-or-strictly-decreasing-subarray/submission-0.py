class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, des = 0,0
        if len(nums) == 0:
            return 0
        res = 1
        direct = "EQUAL"
        j=0
        for i in range(len(nums)-1):
            if direct == "EQUAL":
                if nums[i] < nums[i+1]:
                    direct = "INC"
                    j= i
                    break
                elif nums[i]>nums[i+1]:
                    direct = "DES"
                    j=i
                    break
        print(direct)
        a = 1
        for i in range(j,len(nums)-1):
            if direct == "INC":
                if nums[i]< nums[i+1]:
                    a +=1
                    direct = "INC"
                elif nums[i]> nums[i+1]:
                    a =1
                    direct = "DES" 
                else:
                    a = 1
                    direct = "EQUAL"
            elif direct == "DES":
                if nums[i]< nums[i+1]:
                    a ==1
                    direct = "INC"
                elif nums[i]> nums[i+1]:
                    a +=1
                    direct = "DES" 
                else:
                    a = 1
                    direct = "EQUAL"
            else:
                if nums[i]< nums[i+1]:
                    a =1
                    direct = "INC"
                elif nums[i]> nums[i+1]:
                    a =1
                    direct = "DES" 
                else:
                    a = 1
                    direct = "EQUAL"
            res = max(res,a)
        return res
                
                
