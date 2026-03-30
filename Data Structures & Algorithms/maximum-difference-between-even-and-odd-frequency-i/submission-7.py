class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        o,e = 0,0
        diff = -1000
        for key,value in dic.items():
            if value %2 ==0:
                e = value
            elif value %2 !=0:
                o = value
            if e!=0 and o !=0:
                diff = max(diff,o-e)

        print(dic,diff)
        return diff
        