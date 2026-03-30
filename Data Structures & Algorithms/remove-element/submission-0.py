class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newArr = []
        for i in nums:
            if i != val:
                newArr.append(i)
        nums[:] = newArr
        return len(newArr)