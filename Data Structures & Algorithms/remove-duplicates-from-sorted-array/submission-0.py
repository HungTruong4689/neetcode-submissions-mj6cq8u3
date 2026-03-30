class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        temp = []
        while r < len(nums):
            
            if nums[r]== nums[l]:
                del nums[r]
                r+=1
            else:
                
                r+=1
                l+=1
        print(l)
        if nums[-2] == nums[-1]:
            del nums[-1]
        k =len(nums)
        return k
        