class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkTwoString(a,b):
            dic1 = {}
            dic2 = {}
            for i in a:
                if i not in dic1:
                    dic1[i] = 0
                dic1[i]+=1
            for j in b:
                if j not in dic2:
                    dic2[j] =0
                dic2[j]+=1
            return dic1 == dic2
        n = len(s1)
        for i in range(len(s2)-n+1):
            print(i,n,i+n)
            check = s2[i:i+n]
            print(check)
            if checkTwoString(s1,s2[i:i+n]):
                return True

        return False