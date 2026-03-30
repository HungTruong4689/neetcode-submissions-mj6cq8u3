class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def checkSub(a,b):
            if len(a)<=len(b) and a in b:
                return  a
            elif len(a)>len(b) and b in a:
                return b
            else:
                return ""
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if checkSub(words[i],words[j]) and checkSub(words[i],words[j]) not in res:
                    res.append(checkSub(words[i],words[j]))
        print(checkSub("hero","superhero"))
        return res
                    
        