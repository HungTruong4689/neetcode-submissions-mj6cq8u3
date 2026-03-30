class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in ransomNote:
            if i not in dic:
                dic[i]=0
            dic[i] +=1
        for j in magazine:
            if j in dic:
                dic[j] -=1

        for key,value in dic.items():
            if value >0:
                return False
        return True