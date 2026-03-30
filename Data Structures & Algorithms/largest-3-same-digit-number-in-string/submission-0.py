class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        l,r=0,1
        v = ""
        while r< len(num):
            print(l,r)
            if num[l] !=num[r]:
                v= ""
                l = r
                
                
            else:
                print(l,r)
                if not v:
                    v = num[l]
                if r -l <=2:
                    v += num[l]
                else:
                    l = r
            res = v if v > res else res
            r+=1


        return res if len(res)>=3 else ""