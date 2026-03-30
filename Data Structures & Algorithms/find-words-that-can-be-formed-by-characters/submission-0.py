class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for i in chars:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        res = 0
        k = 0
        for w in words:
            for c in w:
                if c not in dic:
                    k =1
                    break
            if k == 0:
                res += len(w)
            k = 0
        return res