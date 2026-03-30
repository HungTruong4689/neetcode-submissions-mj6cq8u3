class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        o,e = 0,0
        for key,value in dic.items():
            if value %2 ==0 and value>=e:
                e = value
            elif value %2 !=0 and value>=o:
                o = value


        print(dic,o,e)
        return abs(o-e)
        