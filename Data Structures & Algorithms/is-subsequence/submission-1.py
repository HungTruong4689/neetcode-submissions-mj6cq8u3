class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(a:int, b:int) -> bool:
            if a >= len(s):
                return True
            if b >= len(t):
                return False
            
            if s[a] == t[b]:
                return rec(a+1,b+1)
            return rec(a,b+1)
        return rec(0,0)

        