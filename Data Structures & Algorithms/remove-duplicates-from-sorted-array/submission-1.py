class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        temp = []
        while r < len(nums):
            
            if nums[r]== nums[l]:
                del nums[r]
                
            else:
                
                r+=1
                l+=1
        k = len(nums)
        return k
        