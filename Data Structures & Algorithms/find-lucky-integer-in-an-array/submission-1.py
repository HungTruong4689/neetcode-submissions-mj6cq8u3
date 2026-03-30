class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        print(dic)
        result = -1
        for key, value in dic.items():
            if key == value:
                result = max(key,result)
        return result 