class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def checkNumber(nums,target):
            l,r =0,len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m] == target:
                    return True
                if nums[m]>target:
                    r = m -1
                if nums[m]<target:
                    l = m+1
            return False
        for i in matrix:
            if checkNumber(i,target):
                return True
        
               
        return False