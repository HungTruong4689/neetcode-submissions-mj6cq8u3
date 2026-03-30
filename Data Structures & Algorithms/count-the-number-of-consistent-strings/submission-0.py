class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def checkTwoString(a,b):
            s1 = set(a)
            s2 = set(b)
            for i in s2:
                if i not in s1:
                    return False
            return True
        res = 0
        for word in words:
            if checkTwoString(allowed,word):
                res +=1
        return res