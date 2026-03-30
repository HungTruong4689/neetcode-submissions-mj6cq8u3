class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l,r = 0,0
        temp = ""
        m = 0
        while l < len(chars):
            if r < len(chars) and chars[r] == chars[l]:
                r+=1
                m+=1
                if temp == "":
                    temp += chars[l]
                

            else:
                l = r
                if m >1:
                    s += temp + str(m)
                else:
                    s += temp 
                temp = ""
                m = 0
        print(s)
        k = 0
        while k < len(s):
            chars[k] = s[k]
            k+=1
        return len(s)