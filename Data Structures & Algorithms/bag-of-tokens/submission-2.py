class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        tokens.sort()
        l,r = 0,len(tokens)-1
        while l <=r:
            while l<=r and power >= tokens[l]:
                power -= tokens[l]
                res+=1
                l+=1
            if l<=r and res>0:
                power += tokens[r]
                r-=1
                res-=1
        return res
