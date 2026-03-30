class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        self.result = 0
        def rec(a:int,b:int):
            
            if a >= len(s):
                
                self.result = len(t) -b
                
                return self.result
            if b >= len(t):
                return 0
            
            if s[a] == t[b]:
                return rec(a+1,b+1)
            return rec(a+1,b)
        
        return rec(0,0)
        