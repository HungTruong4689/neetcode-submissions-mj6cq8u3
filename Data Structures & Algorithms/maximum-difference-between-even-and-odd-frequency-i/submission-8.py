class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        o,e = [],[]
        diff = -1000
        for key,value in dic.items():
            if value %2 ==0:
                e.append(value)
            elif value %2 !=0:
                o.append(value)
        
        for i in o:
            for j in e:
                diff = max(diff,i-j)

        print(dic,diff)
        return diff
        