class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            prex = w[:len(pref)] if len(w)>= len(pref) else ""
            if prex == pref:
                count +=1
        return count

