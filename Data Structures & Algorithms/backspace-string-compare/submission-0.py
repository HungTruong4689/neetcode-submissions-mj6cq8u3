class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidIndex(st,index):
            backspace = 0
            while index>=0:
                if backspace==0 and st[index] !="#":
                    break
                elif st[index] =="#":
                    backspace +=1
                    
                else:
                    backspace -=1
                index -=1
            print(index)
            return index
        index_s = len(s)-1
        index_t = len(t)-1
        while index_s>= 0 or index_t >=0:
            index_s = nextValidIndex(s,index_s)
            index_t = nextValidIndex(t,index_t)
            char_s = s[index_s] if index_s >=0 else ""
            char_t = t[index_t] if index_t >=0 else ""
            print(char_s,char_t)
            if char_s != char_t:
                return False
            index_s -=1
            index_t -=1
        return True