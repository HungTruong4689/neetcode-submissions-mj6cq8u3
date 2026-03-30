class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set([x for x in range(1,len(nums)+1)])
        s2 = set(nums)
        res= []
        for i in s2:
            if i in s:
                s.remove(i)
        for j in s:
            res.append(j)
        return res