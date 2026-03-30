class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        print(dic)
        result = 0
        for key, value in dic.items():
            if key == value:
                result += 1
        return result if result >0 else -1