class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i,j = 0,1
        m,n =0,0
        while i< len(nums) -1:
            if nums[i]<= nums[i+1]:
                m +=1
            if nums[i]>= nums[i+1]:
                n +=1
            i+=1
       
        
        if m == len(nums)-1 or n == len(nums) -1:
            return True

        return False
        