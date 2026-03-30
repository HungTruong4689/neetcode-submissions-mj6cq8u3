class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ptr, s_ptr = 0 ,0
        #m, n = len(s), len(t)
        while t_ptr < len(t) and s_ptr < len(s):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                s_ptr += 1
        print(s_ptr,t_ptr)
        return  len(t) - t_ptr

        