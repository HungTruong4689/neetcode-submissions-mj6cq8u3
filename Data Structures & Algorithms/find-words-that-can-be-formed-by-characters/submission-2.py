class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for i in chars:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        res = 0
        k = 0
        def checkWord(w,doc):
            temp = doc.copy()
            for c in w:
                if c not in temp:
                    return False
                else:
                    print(c,temp[c])
                    if temp[c]>0:
                        temp[c] -=1
                    else:
                        return False
            return True
        for w in words:
            
            if checkWord(w,dic):
                res += len(w)

            
        return res