class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        sortedDictionary = tuple(sorted(dic.items(),key =lambda item : item[1],reverse=True))
        print(sortedDictionary)
        return [item[0] for item in sortedDictionary[:k]]
        