class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        self.result = 0
        def rec(a:int,b:int):
            
            if a == len(s):
                print("b value "+ str(b))
                self.result = len(t) -b
                print("result "+ str(self.result))
                return False
            if b == len(t):
                return True
            print(s[a], t[b])
            if s[a] == t[b]:
                return rec(a+1,b+1)
            return rec(a+1,b)
        print(rec(0,0))
        return self.result
        