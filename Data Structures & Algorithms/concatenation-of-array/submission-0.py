class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray = nums[:]
        for i in nums:
            newArray.append(i)
        return newArray