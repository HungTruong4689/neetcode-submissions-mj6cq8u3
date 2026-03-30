class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        t = 0
        dic = {}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num] = 1
        for key,value in dic.items():
            if value >=m:
                t = key
                m = value
        return t
        