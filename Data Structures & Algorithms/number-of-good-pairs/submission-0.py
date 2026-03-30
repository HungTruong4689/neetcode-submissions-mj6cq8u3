import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] +=1
        for key,value in dic.items():
            if value >=2:
                res += math.comb(value,2)
        return res
        