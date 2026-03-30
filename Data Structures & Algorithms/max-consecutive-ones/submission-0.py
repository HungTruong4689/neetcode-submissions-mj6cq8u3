class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        length = 0
        for num in nums:
            result = max(length,result)
            if num == 1:
                length +=1
                result = max(length,result)
            if num == 0:
                result = max(length,result)
                length = 0
        return result